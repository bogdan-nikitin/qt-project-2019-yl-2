"""Модуль, содержащий класс вкладки для основной программы, а также все
необходимые классы и функции для его работы"""

import datetime

import pyqtgraph as pg
from PyQt5.QtWidgets import QTabWidget
from PyQt5.QtWidgets import QWidget, QCompleter, QLabel
from numba import jit

from Modules.Currencies import Currencies
from Modules.EasyThreadsQt import queue_thread_qt
from Modules.GetDirectory import get_directory
from UIs.TabWidgetUI import Ui_TabWidget

QUOTES_ACCURACY = 4  # Точность котировок
CHANGE_ACCURACY = 2  # Точность изменения курса
UP_TRIANGLE = '▲'
DOWN_TRIANGLE = '▼'
GREEN = 'green'
RED = 'red'
BLACK = 'black'
# CSS стиль для текста с изменением курса
COURSE_CHANGE_LABEL_STYLESHEET = 'color:{}'
STANDARD_DATE_FORMAT = '%d.%m.%Y'
STANDARD_CURRENCY_PAIR = 'EURRUB'


@jit
def find_nearest(array, value):
    """Функция возвращает индекс наиболее близкого к value числа в массиве array
    Наиболее близким считается число, которое меньше чем value, причём следующее
    число больше, чем value"""
    if value < array[0]:
        return 0
    for i in range(1, len(array)):
        if array[i] > value:
            return i - 1
    return len(array) - 1


@jit
def find_bigger_nearest(array, value):
    """Функция возвращает индекс наиболее близкого к value числа в массиве array
    Наиболее близким считается число, которое больше чем value, причём
    предыдущее число меньше, чем value"""
    for i in range(len(array)):
        if array[i] > value:
            return i
    return len(array) - 1


@jit
def equation_of_line(x1, y1, x2, y2, x):
    """Возвращает значение уравнения прямой по двум точкам
    по значению аргумента"""
    if x1 == x2 and y1 == y2:
        return y1
    elif x2 - x1 == 0:
        return x2
    return (y2 * (x - x1) - y1 * (x - x2)) / (x2 - x1)


def days_to_date(days):
    """Переводит дни в даты, если количетсво дней не слишком большое, иначе
    возвращает None"""
    try:
        return datetime.datetime(1, 1, 1) + datetime.timedelta(days)
    # Исключение, возникающее если количество дней слишком велико
    except OverflowError:
        return


def date_from_days_formatted(value):
    """Возвращает отформатированную дату по количеству дней"""
    date = days_to_date(value)
    if date is None:
        string = ''
    else:
        string = date.strftime(STANDARD_DATE_FORMAT)
    return string


def delete_axis_from_plot_item(orientation, plot_item: pg.PlotWidget):
    """Функция удаляет ось с ориентацией orientaton к графику plotWidget"""
    view_box = plot_item.getViewBox()
    axis = plot_item.axes[orientation]['item']
    axis.linkToView(view_box)
    axis._oldAxis = plot_item.axes[axis.orientation]['item']
    axis._oldAxis.hide()


def attach_to_plot_item(axis: pg.AxisItem, plot_item: pg.PlotWidget):
    """Функция прикрепляет ось AxisItem к графику PlotWidget"""
    axis.setParentItem(plot_item)
    view_box = plot_item.getViewBox()
    axis.linkToView(view_box)
    axis._oldAxis = plot_item.axes[axis.orientation]['item']
    axis._oldAxis.hide()
    plot_item.axes[axis.orientation]['item'] = axis
    pos = plot_item.axes[axis.orientation]['pos']
    plot_item.layout.addItem(axis, *pos)
    axis.setZValue(-1000)


class TimeAxisItem(pg.AxisItem):
    """Временная ось для графика pyqtgraph"""

    def tickStrings(self, values, scale, spacing):
        return list(map(date_from_days_formatted, values))


class CrossHair:
    """Класс перекрестия для графика pyqtgraph. В конструктор передаётся
    график, данные, которые использует график для построения и родитель"""

    def __init__(self, current_plot, data, parent):
        self.vertical_line = pg.InfiniteLine(angle=90, movable=False)
        self.horizontal_line = pg.InfiniteLine(angle=0, movable=False)
        self.current_plot = current_plot
        self.data = data
        self.parent = parent
        self.view_box = self.current_plot.vb
        current_plot.addItem(self.vertical_line, ignoreBounds=True)
        current_plot.addItem(self.horizontal_line, ignoreBounds=True)
        self.proxy = pg.SignalProxy(self.current_plot.scene().sigMouseMoved,
                                    rateLimit=60, slot=self.mouseMoved)

    def mouseMoved(self, event):
        """Метод перемещает перекрестие при движении мыши и устанавливает
        сверху слева текущее значение графика"""
        if len(self.data) < 2:
            self.parent.graphic_value_label.setText('')
            return
        pos = event[0]
        if self.current_plot.sceneBoundingRect().contains(pos):
            mouse_point = self.view_box.mapSceneToView(pos)
            x = mouse_point.x()
            if x < self.data[0][1]:
                x = self.data[0][1]
            elif x > self.data[-1][1]:
                x = self.data[-1][1]
            min_value_index = find_nearest(self.data[:, 1], x)
            max_value_index = find_bigger_nearest(self.data[:, 1], x)
            x1 = self.data[min_value_index][1]
            y1 = self.data[min_value_index][0]
            x2 = self.data[max_value_index][1]
            y2 = self.data[max_value_index][0]
            y = equation_of_line(x1, y1, x2, y2, x)
            date = date_from_days_formatted(x)
            self.parent.graphic_value_label.setText('\n'.join(
                map(str, [round(y, QUOTES_ACCURACY), date])))
            self.vertical_line.setPos(x)
            self.horizontal_line.setPos(y)
            self.current_plot: pg.PlotItem

    def disable(self):
        """Метод отключает перекрестие"""
        self.current_plot.removeItem(self.vertical_line)
        self.current_plot.removeItem(self.horizontal_line)
        self.parent.graphic_value_label.setText('')


class TabWidget(QWidget, Ui_TabWidget):
    """Класс вкладки для основной программы"""

    def __init__(self, tabs_holder=None, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.cross_hair = None
        self.data = []
        self.tabs_holder = tabs_holder
        self.currencies_class = Currencies(get_directory())
        self.currencies = self.currencies_class.currency_pairs()
        self.currency_pair_box.addItems(self.currencies)
        self.currency_pair_box.currentTextChanged.connect(
            self.change_currency_pair_info)
        self.close_btn.clicked.connect(self.close_tab)
        self.currency_pair = self.currency_pair_box.currentText()
        self.currency_pair_box.currentIndexChanged.connect(self.plot_graphic)
        self.currency_pair_box.setCompleter(QCompleter(self.currencies))
        plot_item = self.exchange_rate_graphic.getPlotItem()
        time_axis = TimeAxisItem('bottom')
        attach_to_plot_item(time_axis, plot_item)
        delete_axis_from_plot_item('left', plot_item)
        attach_to_plot_item(pg.AxisItem('right'), plot_item)
        plot_item.getViewBox().setLimits(yMin=0)
        self.set_standard_item()

    def change_currency_pair_info(self, text):
        """Метод меняет информацию о валютной паре во вкладке"""
        name, code = self.currencies_class.currency_pair_info(text)
        self.currency_pair_name_label.setText(name)
        self.currency_pair_char_code.setText(code)
        self.current_quote_label.setText('')
        self.course_change_label.setText('')

    @property
    def tab_widget(self) -> QTabWidget:
        """Свойство, возвращающее объект QTabWidget своего главного окна"""
        if self.tabs_holder:
            return self.tabs_holder.tab_widget

    @property
    def tab_index(self):
        """Свойство, возвращающее собственный индекс в объекте QTabWidget
        своего главного окна"""
        if self.tab_widget:
            return self.tab_widget.indexOf(self)

    def plot_graphic(self):
        """Метод отвечает за построение графика и перекрестия"""
        self.cross_hair = None
        self.thread_plot_graphic()
        # Декоратор, возвращающийся в результате работы функциии queue_thread_qt
        # содержит поле thread, хранящее поток, в котором выполняется
        # построение графика
        thread = self.thread_plot_graphic.thread
        # По завершению потока строим перекрестие, т.к. при построении его
        # в потоке оно не работает
        thread.finished.connect(self.enable_cross_hair)

    @queue_thread_qt  # Метод работает в отдельной очереди потоков
    def thread_plot_graphic(self):
        """Метод вычисляет котировки валют и строит по ним график"""
        currency_pair = self.currency_pair_box.currentText()
        self.currency_pair = currency_pair
        if self.tab_widget:
            self.tab_widget.setTabText(self.tab_index, currency_pair)
        data = self.currencies_class.quotes_of_currency_pair(currency_pair)
        self.data = data
        if self.currency_pair_box.currentText() != currency_pair:
            return
        view_box = self.exchange_rate_graphic.getPlotItem().getViewBox()
        view_box.enableAutoRange(axis='x')
        view_box.enableAutoRange(axis='y')
        self.exchange_rate_graphic.clear()
        self.exchange_rate_graphic.plot(data[:, 1], data[:, 0])

        if len(data) > 0:
            self.current_quote_label.setText(str(round(data[-1][0],
                                                       CHANGE_ACCURACY)))
        if len(data) >= 2:
            difference = data[-1][0] - data[-2][0]
            percent_difference = difference / data[-2][0] * 100
            if difference > 0:
                triangle = UP_TRIANGLE
                color = GREEN
            elif difference < 0:
                triangle = DOWN_TRIANGLE
                color = RED
            else:
                triangle = ''
                color = BLACK
            sign = '+' if difference > 0 else ''
            self.course_change_label.setText(
                f'{sign}{difference:.2f} '
                f'({sign}{percent_difference:.2f}%) {triangle}')
        else:
            self.course_change_label.setText('')
            color = BLACK
        label_class = QLabel.__name__
        style_sheet = COURSE_CHANGE_LABEL_STYLESHEET.format(color)
        self.course_change_label.setStyleSheet(
            f'{label_class}{{{style_sheet}}}')

    def enable_cross_hair(self):
        """Метод включает перекрестие"""
        if self.tabs_holder and self.tabs_holder.is_cross_hair_enabled:
            self.add_cross_hair()

    def add_cross_hair(self):
        """Метод добавляет перекрестие к графику"""
        self.cross_hair = CrossHair(self.exchange_rate_graphic.getPlotItem(),
                                    self.data, self)

    def disable_cross_hair(self):
        """Метод отключает перекрестие"""
        self.cross_hair.disable()
        self.cross_hair = None

    def get_name(self):
        """Метод возвращает имя для отображения во вкладках. В качестве имени
        используется название валютной пары"""
        return self.currency_pair

    def close_tab(self):
        """Метод закрывает текущую вкладку"""
        if self.tab_widget:
            index = self.tab_index
            self.tabs_holder.close_tab(index)

    def set_standard_item(self):
        """Метод выставляет в currency_pair_box стандартную валютную пару,
        указанную в переменной STANDART_CURRENCY_PAIR"""
        if STANDARD_CURRENCY_PAIR in self.currencies:
            index = self.currencies.index(STANDARD_CURRENCY_PAIR)
            self.currency_pair_box.setCurrentIndex(index)

    def reset_tab(self):
        """Метод возвращает вкладку к изначальному состоянию
        (к моменту создания)"""
        self.set_standard_item()
        self.plot_graphic()
