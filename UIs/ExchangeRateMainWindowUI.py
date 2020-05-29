# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIs/ExchangeRateMainWindowUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ExchangeRateMainWindow(object):
    def setupUi(self, ExchangeRateMainWindow):
        ExchangeRateMainWindow.setObjectName("ExchangeRateMainWindow")
        ExchangeRateMainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(ExchangeRateMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tab_widget = QtWidgets.QTabWidget(self.centralwidget)
        self.tab_widget.setUsesScrollButtons(True)
        self.tab_widget.setDocumentMode(False)
        self.tab_widget.setTabsClosable(False)
        self.tab_widget.setMovable(True)
        self.tab_widget.setObjectName("tab_widget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tab_widget.addTab(self.tab, "")
        self.gridLayout.addWidget(self.tab_widget, 0, 0, 1, 1)
        ExchangeRateMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ExchangeRateMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.view_menu = QtWidgets.QMenu(self.menubar)
        self.view_menu.setObjectName("view_menu")
        self.help_menu = QtWidgets.QMenu(self.menubar)
        self.help_menu.setObjectName("help_menu")
        ExchangeRateMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ExchangeRateMainWindow)
        self.statusbar.setObjectName("statusbar")
        ExchangeRateMainWindow.setStatusBar(self.statusbar)
        self.cross_hair_action = QtWidgets.QAction(ExchangeRateMainWindow)
        self.cross_hair_action.setObjectName("cross_hair_action")
        self.help_action = QtWidgets.QAction(ExchangeRateMainWindow)
        self.help_action.setObjectName("help_action")
        self.about_action = QtWidgets.QAction(ExchangeRateMainWindow)
        self.about_action.setObjectName("about_action")
        self.view_menu.addAction(self.cross_hair_action)
        self.help_menu.addAction(self.help_action)
        self.help_menu.addAction(self.about_action)
        self.menubar.addAction(self.view_menu.menuAction())
        self.menubar.addAction(self.help_menu.menuAction())

        self.retranslateUi(ExchangeRateMainWindow)
        self.tab_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ExchangeRateMainWindow)

    def retranslateUi(self, ExchangeRateMainWindow):
        _translate = QtCore.QCoreApplication.translate
        ExchangeRateMainWindow.setWindowTitle(_translate("ExchangeRateMainWindow", "Графики курсов валют"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab), _translate("ExchangeRateMainWindow", "+"))
        self.view_menu.setTitle(_translate("ExchangeRateMainWindow", "Вид"))
        self.help_menu.setTitle(_translate("ExchangeRateMainWindow", "Справка"))
        self.cross_hair_action.setText(_translate("ExchangeRateMainWindow", "Перекрестие"))
        self.help_action.setText(_translate("ExchangeRateMainWindow", "Помощь"))
        self.about_action.setText(_translate("ExchangeRateMainWindow", "О программе"))
