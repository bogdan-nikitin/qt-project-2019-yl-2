"""Главный файл приложения"""

import sys
import os
import shutil
from Modules.ExchangeRateMainWindow import ExchangeRateMainWindow
from PyQt5.QtWidgets import QApplication, QMessageBox


DATABASES_FOLDER = 'Databases'
MESSAGE_BOX_TEXT = 'Произошла ошибка'
MESSAGE_BOX_INFORMATIVE_TEXT = ('В прошлый раз программа завершила свою '
                                'работу неккоректно. Неисправные файлы '
                                'программы были удалены.')
MESSAGE_BOX_TITLE = 'Ошибка'
LOG_FILE_PATH = 'log.txt'


def write_log(text):
    """Запись текста text в файл LOG_FILE_PATH"""
    with open(LOG_FILE_PATH, mode='w') as file:
        file.write(text)


def read_log():
    """Чтение и возврат текста из файла LOG_FILE_PATH"""
    if os.path.isfile(LOG_FILE_PATH):
        with open(LOG_FILE_PATH) as file:
            return file.read()
    return '0'


def show_error_message():
    """Показывает окно с ошибкой о неудачном предыдущем запуске"""
    error_message_box = QMessageBox()
    error_message_box.setIcon(QMessageBox.Critical)
    error_message_box.setText(MESSAGE_BOX_TEXT)
    error_message_box.setInformativeText(MESSAGE_BOX_INFORMATIVE_TEXT)
    error_message_box.setWindowTitle(MESSAGE_BOX_TITLE)
    error_message_box.setStandardButtons(QMessageBox.Ok)
    error_message_box.exec()
    return error_message_box


def delete_folder(folder):
    """Удаляет папку"""
    if not os.path.exists(folder) or not os.path.isdir(folder):
        return
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        if os.path.isfile(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)


if __name__ == '__main__':
    # Как я заметил, программа падает молча, не выдавая исключений, но на
    # всякий случай оставил эту проверку
    try:
        # Попытка запустить программу
        app = QApplication(sys.argv)
        log = read_log()
        if log != '0':
            # Удаление папки с базами данных, так как ошибки в основном
            # возникают при порче базы данных
            # В БД просто кэшируются данные, полученные во время работы
            # программы, так что мы можем их спокойно удалить
            delete_folder(DATABASES_FOLDER)
            # Вывод сообщения об ошибке, если программа в прошлый раз
            # запустилась неккоректно
            msg = show_error_message()
        # Будем считать, что если программа не завершилась удачно, то значит
        # она завершилась неудачно
        write_log('-1')
        window = ExchangeRateMainWindow()
        window.show()
        exit_code = app.exec()
        # Запись в лог результата работы программы
        write_log(str(exit_code))
        sys.exit(exit_code)
    except Exception as error_code:
        # В случае ошибки запись в лог текста ошибки
        write_log(str(error_code))
        raise error_code
