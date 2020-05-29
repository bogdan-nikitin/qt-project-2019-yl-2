from UIs.ExchangeRateMainWindowUI import Ui_ExchangeRateMainWindow
from Modules.TabWidget import TabWidget
from Modules.Forms import HelpWidget, AboutWidget
from PyQt5.QtWidgets import QMainWindow, QTabWidget


MARK = '✓'


class ExchangeRateMainWindow(QMainWindow, Ui_ExchangeRateMainWindow):
    """Класс главного окна программы"""
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.tab_widget: QTabWidget = self.tab_widget
        self.cross_hair_action_text = self.cross_hair_action.text()
        self.is_cross_hair_enabled = True
        self.change_cross_hair_action_text()
        self.add_tab()
        self.tab_widget.currentChanged.connect(self.add_tab)
        self.cross_hair_action.triggered.connect(self.change_cross_hair)
        self.help = HelpWidget()
        self.about = AboutWidget()
        self.help.hide()
        self.about.hide()
        self.help_action.triggered.connect(self.show_help)
        self.about_action.triggered.connect(self.show_about)

    def add_tab(self, index=None):
        """Добавление новой вкладки"""
        if index is not None and index != self.tab_widget.count() - 1:
            return
        index = self.tab_widget.count() - 1
        tab = TabWidget(self)
        self.tab_widget.insertTab(index, tab, tab.get_name())
        self.tab_widget.setCurrentIndex(index)

    def close_tab(self, index):
        """Закрытие вкладки по индексу"""
        widget = self.tab_widget.widget(index)
        if index == self.tab_widget.count() - 2:
            self.tab_widget.setCurrentIndex(index - 1)
        self.tab_widget.removeTab(index)
        widget.deleteLater()

    def change_cross_hair(self):
        """Включение/выключение перекрестия"""
        self.is_cross_hair_enabled = not self.is_cross_hair_enabled
        self.change_cross_hair_action_text()
        for i in range(self.tab_widget.count() - 1):
            tab = self.tab_widget.widget(i)
            if self.is_cross_hair_enabled:
                tab.add_cross_hair()
            else:
                tab.disable_cross_hair()

    def change_cross_hair_action_text(self):
        """Смена надписи в строке меню "Вид" в пункте "Перекрестие". В случае,
        если перекрестие включено, добавляется галочка, а иначе она убирается"""
        if self.is_cross_hair_enabled:
            self.cross_hair_action.setText(self.cross_hair_action_text + ' ' +
                                           MARK)
        else:
            self.cross_hair_action.setText(self.cross_hair_action_text)

    def show_help(self):
        """Показать окно помощи"""
        self.help.show()

    def show_about(self):
        """Показать окно "О программе"/"""
        self.about.show()
