"""Модуль для простой работы с потоками в PyQt5"""

import typing

from PyQt5.QtCore import QThread
from multimethod import multimethod


class SimpleThreadQt(QThread):
    """Простой поток, принимающий фунцию и аргументы, которые следует в неё
    передать при запуске потока. Результат работы функции записывается в атрибут
    result объекта класса. Запуск потока осуществляется через метод start"""

    def __init__(self, function, function_args, function_kwargs,
                 *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.function = function
        self.function_args = function_args
        self.function_kwargs = function_kwargs
        self.result = None

    def run(self):  # Метод, вызывающийся при запуске потока
        self.result = self.function(*self.function_args, **self.function_kwargs)

    """Получить результат работы функции"""

    def get_result(self):
        return self.result


def simple_thread_qt(func):
    """Декоратор, возвращающий функцию, которая запускает переданную в декоратор
    функцию function в потоке SimpleThreadQt. Декоратор передаёт поток в
    атрибут функции _thread"""

    def function_in_thread(*args, **kwargs):
        thread = SimpleThreadQt(func, args, kwargs)
        function_in_thread.thread = thread
        thread.start()

    return function_in_thread


class QueueThreadQt(QThread):
    """Поток, выполняющий поочерёдно функции с одинаковым тегом, передающимся
    в конструктор. Предназначен для работы с функциями, которые изменяют
    один и тот же объект(например, вставляют значения в одну и ту же базу
    данных). Запуск потока осуществляется через метод begin"""
    queues = {}

    def __init__(self, func, function_args, function_kwargs, tag='',
                 *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.function = func
        self.function_args = function_args
        self.function_kwargs = function_kwargs
        self.result = None
        self.tag = tag
        queues = QueueThreadQt.queues
        if tag not in queues:
            queues[tag] = []
        queues[tag] += [self]
        self.finished.connect(self.on_finish)

    def run(self):
        self.result = self.function(*self.function_args, **self.function_kwargs)

    """Получить результат работы функции"""

    def get_result(self):
        return self.result

    def on_finish(self):
        """Метод запускает следующую функцию в очереди с одинаковым тегом,
        если таковая имеется"""
        QueueThreadQt.queues[self.tag] = QueueThreadQt.queues[self.tag][1:]
        queue = QueueThreadQt.queues[self.tag]
        if len(queue) > 0:
            thread = queue[0]
            thread.start()

    @staticmethod
    def begin_by_tag(tag):
        """Запуск функции с определённым тегом (не требует объекта потока)"""
        if tag in QueueThreadQt.queues:
            QueueThreadQt.queues[tag].begin()

    def begin(self):
        """Запуск выполнения функции"""
        queue = QueueThreadQt.queues[self.tag]
        if len(queue) == 1:
            queue[0].start()


@multimethod
def queue_thread_qt(tag: str = ''):
    """Функция, возвращающая декоратор, запускающий фунцию в потоке
    QueueThreadQt с тегом tag(если тег не указан, то тегом становится название
    функции)"""

    def queue_thread_qt_decorator(func):
        """Декоратор, запускающий функцию в потоке QueueThreadQt с тегом
        tag(если тег не указан, то тегом становится название функции). Поток
        записывается в атрибут _thread функции function"""

        def function_in_thread(*args, **kwargs):
            thread = QueueThreadQt(func, args, kwargs, tag)
            function_in_thread.thread = thread
            thread.begin()

        return function_in_thread

    return queue_thread_qt_decorator


@multimethod
def queue_thread_qt(func: typing.Callable):
    return queue_thread_qt(func.__name__)(func)
