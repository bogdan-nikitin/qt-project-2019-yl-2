"""Модуль, содержащий основные функции, константы, классы для работы с
котировками и БД"""

import datetime
import itertools
import operator
import os
import sqlite3
import typing
import xml.dom.minidom

import numpy as np
import requests
from multimethod import multimethod
from numba import jit

CURRENCY_CODES_URL = 'http://www.cbr.ru/scripts/XML_valFull.asp'
CURRENCY_VALUES_URL = 'http://www.cbr.ru/scripts/XML_dynamic.asp'
CODES_TABLE_CREATE_REQUEST = '''CREATE TABLE codes (
    id        INTEGER PRIMARY KEY AUTOINCREMENT
                      UNIQUE
                      NOT NULL,
    currency_id STRING  UNIQUE
                      NOT NULL,
    char_code STRING  NOT NULL
                      UNIQUE,
    name      STRING  NOT NULL  UNIQUE,
    nominal     INTEGER  NOT NULL
);'''
CURRENCY_PAIR_TABLE_CREATE_REQUEST = '''CREATE TABLE currency_pair (
    id        INTEGER PRIMARY KEY AUTOINCREMENT
                      UNIQUE
                      NOT NULL,
    quotation REAL,
    date      DATE    UNIQUE
                      NOT NULL
);'''
CURRENCY_TABLE_CREATE_REQUEST = '''CREATE TABLE quotations (
    id    INTEGER PRIMARY KEY AUTOINCREMENT
                  NOT NULL
                  UNIQUE,
    value REAL    NOT NULL,
    days  INTEGER NOT NULL UNIQUE
);'''
CODES_INSERT_REQUEST = '''INSERT INTO 
codes(currency_id, char_code, name, nominal) 
SELECT ?, ?, ?, ? WHERE NOT EXISTS 
(SELECT currency_id, char_code, name, nominal FROM codes 
WHERE currency_id=? OR char_code=? OR name=?)'''
CURRENCY_INSERT_REQUEST = '''INSERT INTO quotations(value, days) SELECT ?, ? 
WHERE NOT EXISTS (SELECT days FROM quotations WHERE days=?)'''
DATABASES_FOLDER_NAME = 'Databases'
CURRENCIES_FOLDER_NAME = 'currencies'
CURRENCY_PAIRS_FOLDER_NAME = 'currency_pairs'
CURRENCY_CODES_DB_NAME = 'currency_codes.db'
CURRENCY_TAG = 'Item'
CURRENCY_ID_ATTRIBUTE = 'ID'
CHAR_CODE_TAG = 'ISO_Char_Code'
NAME_TAG = 'Name'
NOMINAL_TAG = 'Nominal'
RECORD_TAG = 'Record'
VALUE_TAG = 'Value'
DATE_ATTRIBUTE = 'Date'
MISSING_CHAR_CODES = {'R01436': 'LTT',
                      'R01720A': 'UAK'}
# Самая ранняя дата, с которой с сайта ЦБР можно получить котировки
START_DATE = datetime.datetime(1753, 1, 1)  # 01/01/1753
ZERO_DATE = datetime.datetime(1, 1, 1)
RUB_CHAR_CODE = 'RUB'
NOMINAL_FIELD = 'nominal'
CURRENCY_ID_FIELD = 'currency_id'
NAME_FIELD = 'name'
RUB_NAME = 'Российский рубль'
URL_DATE_FORMAT = '%d/%m/%Y'
ATTRIBUTE_DATE_FORMAT = '%d.%m.%Y'


# Две следующие функции не используются, но вполне возможно будут использованы
# в дальнейших обновлениях программы
@jit
def elements_difference(array: np.array):
    """Возвращает массив разностей между элементами массива array.
    Например, для массива [5, 4, 3, 2, 1] массив разностей будет следующим:
    [5 - 4, 4 - 3, 3 - 2, 2 - 1] (или [1, 1, 1, 1])"""
    difference_array_size = array.shape[0] - 1
    difference_array = np.zeros(difference_array_size)
    for i in range(difference_array_size):
        difference_array[i] = array[i] - array[i + 1]
    return difference_array


@jit
def elements_percent_difference(array: np.array):
    """Возвращает массив разностей между элементами массива array в процентах.
    Например, для массива [32, 16, 8, 4, 2] массив разностей в процентах
    будет следующим: [50, 50, 50, 50, 50]"""
    difference_array_size = array.shape[0] - 1
    difference_array = np.zeros(difference_array_size)
    for i in range(difference_array_size):
        difference_array[i] = (array[i] - array[i + 1]) / array[i] * 100
    return difference_array


def currencies(currency_pair: str):
    """Разделяет строку с названием валютной пары на строки, содержащие названия
    валют"""
    return currency_pair[:3], currency_pair[3:]


def create_empty_file(full_path: str):
    """Создаёт пустой файл в указанной директории и саму директорию"""
    full_path = full_path.replace('\\', '/')
    path = '/'.join(full_path.split('/')[:-1])
    if not os.path.isdir(path):
        os.makedirs(path)
    open(full_path, mode='w').close()


def datetime_to_days(datetime_object: datetime):
    """Конвертирует объект datetime в дни"""
    if type(datetime_object) is datetime.date:
        date = datetime.datetime(datetime_object.year,
                                 datetime_object.month,
                                 datetime_object.day)
    else:
        date = datetime_object
    return (date - ZERO_DATE).days


def now_date():
    """Возвращает сегодняшнюю дату"""
    current_date = datetime.datetime.now()
    date_value = datetime.date(current_date.year,
                               current_date.month,
                               current_date.day)
    return date_value


def object_range(start, end, step):
    """Генератор по типу range для объектов. Прибавляет step к start до тех пор,
     пока start меньше end"""
    current = start
    while current < end:
        yield current
        current += step


@multimethod
def date_range(start: datetime.datetime,
               end: datetime.datetime,
               step: datetime.timedelta) -> object_range:
    """Генератор по типу range для дат. Генерирует даты в промежутке
    [start, end) с шагом step (либо datetime.timedelta(step), если step
    относится к типу int)
    Возвращает генератор object_range, где start=start(или MINIMAL_DATE, если
    передан только один аргумент), end=end и
    step=step (либо datetime.timedelta(step), если step относится к типу int)"""
    return object_range(start, end, step)


@multimethod
def date_range(start: datetime.datetime,
               end: datetime.datetime,
               step: int) -> object_range:
    return date_range(start, end, datetime.timedelta(step))


@multimethod
def date_range(start: datetime.datetime,
               end: datetime.datetime) -> object_range:
    # Если шаг не указан, то выставляем шаг в один день
    return date_range(start, end, 1)


@multimethod
def date_range(end: typing.Optional[datetime.datetime]) -> object_range:
    return date_range(ZERO_DATE, end)


class Currencies:
    """Класс для работы с валютами: получения котировок, создания баз данных
    с информацией о валютах. В конструктор принимает директорию, в которой
    будет вестись работа с базами данных"""

    def __init__(self, directory: str):
        self.directory = directory

    @property
    def database_path(self) -> str:
        """Свойство, возвращающее путь к папке с базами данных"""
        return '/'.join([self.directory,
                         DATABASES_FOLDER_NAME])

    def create_currency_codes_database(self) -> None:
        """Метод создаёт базу данных с названием, записанным в
        CURRENCY_CODES_DB_NAME, по пути
        *директория, переданная в конструктор*/DATABASES_FOLDER_NAME
        в которой содержится информация о валютах:
        их идентификатор в ЦБР, код ISO, название и номинал."""
        database_path = self.database_path + '/' + CURRENCY_CODES_DB_NAME
        create_empty_file(database_path)
        con = sqlite3.connect(database_path)
        cur = con.cursor()
        cur.execute(CODES_TABLE_CREATE_REQUEST)
        # Получаем коды с ЦБР с помощью requests и парсим полученный ответ
        codes = requests.get(CURRENCY_CODES_URL).text
        doc = xml.dom.minidom.parseString(codes)
        for currency in doc.getElementsByTagName(CURRENCY_TAG):
            currency: xml.dom.minidom.Element = currency
            currency_id = currency.getAttribute(CURRENCY_ID_ATTRIBUTE)
            char_code_element = currency.getElementsByTagName(
                CHAR_CODE_TAG)[0].firstChild
            if char_code_element is None:
                char_code = MISSING_CHAR_CODES.get(currency_id)
            else:
                char_code = char_code_element.nodeValue
            if char_code is None:
                continue
            name = currency.getElementsByTagName(NAME_TAG)[
                0].firstChild.nodeValue
            nominal = currency.getElementsByTagName(NOMINAL_TAG)[
                0].firstChild.nodeValue
            cur.execute(CODES_INSERT_REQUEST,
                        ([currency_id, char_code, name, nominal] * 2)[:-1])

        con.commit()
        con.close()

    def check_currency_codes_database(self) -> bool:
        """Метод провиляет наличие базы данных с информацией о валютах"""
        database_path = self.database_path + '/' + CURRENCY_CODES_DB_NAME
        if not os.path.isfile(database_path):
            return False
        return True

    def currency_pairs(self) -> typing.List[str]:
        """Возвращает список валютных пар"""
        database_path = self.database_path + '/' + CURRENCY_CODES_DB_NAME
        if not self.check_currency_codes_database():
            self.create_currency_codes_database()
        con = sqlite3.connect(database_path)
        cur = con.cursor()
        char_codes = list(map(operator.itemgetter(0),
                              cur.execute('SELECT char_code FROM codes').
                              fetchall())) + [RUB_CHAR_CODE]
        pairs = list(map(''.join, itertools.permutations(char_codes, r=2)))
        return sorted(pairs)

    def get_by_char_code(self, currency_char_code, field):
        """Метод возвращает поле field из базы данных DATABASES_FOLDER_NAME"""
        if not self.check_currency_codes_database():
            self.create_currency_codes_database()
        con = sqlite3.connect('/'.join([self.database_path,
                                        CURRENCY_CODES_DB_NAME]))
        cur = con.cursor()
        value = cur.execute('SELECT {} FROM codes '
                            'WHERE char_code = "{}"'.
                            format(field, currency_char_code)).fetchone()
        con.close()
        if value and len(value) > 0:
            return value[0]

    def currency_path(self, currency) -> str:
        """Путь к базе данных валюты currency"""
        return '/'.join([self.database_path,
                         CURRENCIES_FOLDER_NAME,
                         currency + '.db'])

    def check_quotations(self, currency) -> bool:
        """Проверка существования котировок для валюты currency"""
        database_path = self.currency_path(currency)
        return os.path.isfile(database_path)

    def create_quotations(self, currency) -> None:
        """Метод создаёт котировки валюты с кодом ISO, записанным в аргумент
        currency"""
        database_path = self.currency_path(currency)
        create_empty_file(database_path)
        con = sqlite3.connect(database_path)
        cur = con.cursor()
        cur.execute(CURRENCY_TABLE_CREATE_REQUEST)
        con.close()
        self.update_quotations(currency)

    def update_quotations(self, currency) -> None:
        """Метод обновляет котировки валюты с кодом ISO, равным currency"""
        if not self.check_quotations(currency):
            return
        database_path = self.currency_path(currency)
        con = sqlite3.connect(database_path)
        cur = con.cursor()
        start_date_value = cur.execute(
            'SELECT days FROM quotations ORDER BY days DESC').fetchone()
        if start_date_value is None:
            start = START_DATE

        else:
            start_date = (ZERO_DATE +
                          datetime.timedelta(days=start_date_value[0] + 1))
            if start_date < START_DATE:
                start = START_DATE
            else:
                start = start_date
        formatted_date = start.strftime(URL_DATE_FORMAT)
        current_date = datetime.datetime.now()
        if currency == RUB_CHAR_CODE:
            for date in date_range(start,
                                   current_date + datetime.timedelta(days=1)):
                days = (date - datetime.datetime(1, 1, 1)).days
                cur.execute('INSERT INTO quotations(value, days) VALUES(?, ?)',
                            (1, days))
        currency_id = self.get_by_char_code(currency, CURRENCY_ID_FIELD)
        currency_nominal = self.get_by_char_code(currency, NOMINAL_FIELD)
        currency_values_xml = requests.get(
            CURRENCY_VALUES_URL,
            params={'date_req1': formatted_date,
                    'date_req2': current_date.strftime(URL_DATE_FORMAT),
                    'VAL_NM_RQ': currency_id}
        ).text
        currency_values_doc = xml.dom.minidom.parseString(currency_values_xml)
        for record in currency_values_doc.getElementsByTagName(RECORD_TAG):
            record: xml.dom.minidom.Element = record
            value = (np.float(record.getElementsByTagName(VALUE_TAG)[0].
                              firstChild.nodeValue.replace(',', '.')) /
                     currency_nominal)
            date_time = datetime.datetime.strptime(
                record.getAttribute(DATE_ATTRIBUTE), ATTRIBUTE_DATE_FORMAT)
            date = datetime.date(date_time.year, date_time.month, date_time.day)
            days = datetime_to_days(date)
            cur.execute(CURRENCY_INSERT_REQUEST, (value, days, days))
        con.commit()
        con.close()

    def quotes_of_currency(self,
                           currency) -> typing.List[typing.Tuple[float, int]]:
        """Возвращает котировки валюты в виде списка пар значение-дата, где
        дата - это кол-во дней, прошедших с 1.01.0001."""
        # Проверяем, существуют ли котировки для заданной валюты, и если нет,
        # то создаём их, а иначе считываем из БД
        if not self.check_quotations(currency):
            self.create_quotations(currency)
        con = sqlite3.connect(self.currency_path(currency))
        cur = con.cursor()
        # Находим последнюю дату, для которой получены котировки
        last_day_value = cur.execute('SELECT days FROM quotations '
                                     'ORDER BY days DESC').fetchone()
        if not last_day_value:
            last_day = 0
        else:
            last_day = last_day_value[0]
        current_day = datetime_to_days(datetime.datetime.now())
        # Если дата последней котировки не совпадает с текущей, обновляем
        # котировки
        if last_day != current_day:
            con.close()
            self.update_quotations(currency)
            con = sqlite3.connect(self.currency_path(currency))
            cur = con.cursor()
        # Получаем список котировок из БД и возвращаем его
        table_values = cur.execute('SELECT value, days '
                                   'FROM quotations ORDER BY days')
        if not table_values:
            return []
        values = list(table_values.fetchall())
        return values

    def quotes_of_currency_pair(
            self, currency_pair: str
    ) -> typing.Optional[np.ndarray]:
        """Возвращает котировки валютной пары. Если указанная пара
        недействительна, возвращает None."""
        # Название любой валютной пары должно состоять из 6 символов (к
        # примеру USDRUB). Если это не так, возвращаем None
        if len(currency_pair) != 6:
            return
        base_currency, quote_currency = currencies(currency_pair)
        base_quotations = np.array(self.quotes_of_currency(base_currency))
        quote_quotations = np.array(self.quotes_of_currency(quote_currency))
        if not all(map(len, [base_quotations, quote_quotations])):
            return np.array([[0, 0]])
        days = np.intersect1d(base_quotations[:, 1], quote_quotations[:, 1])
        mask_for_base = np.in1d(base_quotations[:, 1], days)
        mask_for_quote = np.in1d(quote_quotations[:, 1], days)
        masked_base_quotations = base_quotations[mask_for_base][:, 0]
        masked_quote_quotations = quote_quotations[mask_for_quote][:, 0]
        quotations = masked_base_quotations / masked_quote_quotations
        return np.column_stack((quotations, days))

    def currency_pair_info(self, currency_pair):  # -> typing.Tuple[str, str]:
        """Возвращает информацию о валютной паре: кортеж из названий каждой
        валюты через слеш и кодов ISO каждой валюты через слеш. Если валютная
        пара недействительна, возвращает кортеж из двух пустых строк."""
        if len(currency_pair) != 6:
            return '', ''
        base_currency, quote_currency = currencies(currency_pair)
        if base_currency == quote_currency:
            return '', ''
        if base_currency == RUB_CHAR_CODE:
            base_currency_name = RUB_NAME
        else:
            base_currency_name = self.get_by_char_code(base_currency,
                                                       NAME_FIELD)
        if quote_currency == RUB_CHAR_CODE:
            quote_currency_name = RUB_NAME
        else:
            quote_currency_name = self.get_by_char_code(quote_currency,
                                                        NAME_FIELD)
        if any(map(lambda v: v is None, [base_currency, base_currency_name,
                                         quote_currency, quote_currency_name])):
            return '', ''
        # Пришлось убрать аннотацию типа возвращаемого значения этой функции,
        # т.к. PyCharm не в силах понять, что тип этого:
        return tuple(map('/'.join, [[base_currency_name, quote_currency_name],
                                    [base_currency, quote_currency]]))
        # - как раз typing.Tuple[str, str]
