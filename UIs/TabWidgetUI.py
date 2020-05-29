# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIs/TabWidgetUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TabWidget(object):
    def setupUi(self, TabWidget):
        TabWidget.setObjectName("TabWidget")
        TabWidget.resize(762, 703)
        self.verticalLayout = QtWidgets.QVBoxLayout(TabWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.currency_pair_name_label = QtWidgets.QLabel(TabWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.currency_pair_name_label.setFont(font)
        self.currency_pair_name_label.setText("")
        self.currency_pair_name_label.setObjectName("currency_pair_name_label")
        self.horizontalLayout.addWidget(self.currency_pair_name_label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.close_btn = QtWidgets.QToolButton(TabWidget)
        self.close_btn.setObjectName("close_btn")
        self.horizontalLayout.addWidget(self.close_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.currency_pair_char_code = QtWidgets.QLabel(TabWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.currency_pair_char_code.setFont(font)
        self.currency_pair_char_code.setText("")
        self.currency_pair_char_code.setObjectName("currency_pair_char_code")
        self.horizontalLayout_2.addWidget(self.currency_pair_char_code)
        self.current_quote_label = QtWidgets.QLabel(TabWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.current_quote_label.setFont(font)
        self.current_quote_label.setText("")
        self.current_quote_label.setObjectName("current_quote_label")
        self.horizontalLayout_2.addWidget(self.current_quote_label)
        self.course_change_label = QtWidgets.QLabel(TabWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.course_change_label.setFont(font)
        self.course_change_label.setStyleSheet("")
        self.course_change_label.setText("")
        self.course_change_label.setObjectName("course_change_label")
        self.horizontalLayout_2.addWidget(self.course_change_label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.currency_pair_box = QtWidgets.QComboBox(TabWidget)
        self.currency_pair_box.setEditable(True)
        self.currency_pair_box.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.currency_pair_box.setObjectName("currency_pair_box")
        self.horizontalLayout_3.addWidget(self.currency_pair_box)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.graphic_value_label = QtWidgets.QLabel(TabWidget)
        self.graphic_value_label.setText("")
        self.graphic_value_label.setObjectName("graphic_value_label")
        self.horizontalLayout_3.addWidget(self.graphic_value_label)
        self.horizontalLayout_3.setStretch(0, 2)
        self.horizontalLayout_3.setStretch(1, 12)
        self.horizontalLayout_3.setStretch(2, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.exchange_rate_graphic = PlotWidget(TabWidget)
        self.exchange_rate_graphic.setObjectName("exchange_rate_graphic")
        self.verticalLayout.addWidget(self.exchange_rate_graphic)

        self.retranslateUi(TabWidget)
        QtCore.QMetaObject.connectSlotsByName(TabWidget)

    def retranslateUi(self, TabWidget):
        _translate = QtCore.QCoreApplication.translate
        TabWidget.setWindowTitle(_translate("TabWidget", "Tab"))
        self.close_btn.setText(_translate("TabWidget", "x"))
from pyqtgraph import PlotWidget
