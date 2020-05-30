"""Модуль, содержащий дополнительные окна приложения"""

from PyQt5.QtWidgets import QWidget

from UIs.AboutFormUI import Ui_AboutForm
from UIs.HelpFormUI import Ui_HelpForm


class AboutWidget(QWidget, Ui_AboutForm):
    """Класс окна с информацией о программе"""

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)


class HelpWidget(QWidget, Ui_HelpForm):
    """Класс окна с помощью"""

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
