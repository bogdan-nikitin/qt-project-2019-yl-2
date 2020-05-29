# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIs/AboutFormUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AboutForm(object):
    def setupUi(self, AboutForm):
        AboutForm.setObjectName("AboutForm")
        AboutForm.resize(810, 203)
        self.verticalLayout = QtWidgets.QVBoxLayout(AboutForm)
        self.verticalLayout.setObjectName("verticalLayout")
        self.text_browser = QtWidgets.QTextBrowser(AboutForm)
        self.text_browser.setStyleSheet("QTextBrowser{background-color: rgba(0, 0, 0, 0)}")
        self.text_browser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.text_browser.setObjectName("text_browser")
        self.verticalLayout.addWidget(self.text_browser)

        self.retranslateUi(AboutForm)
        QtCore.QMetaObject.connectSlotsByName(AboutForm)

    def retranslateUi(self, AboutForm):
        _translate = QtCore.QCoreApplication.translate
        AboutForm.setWindowTitle(_translate("AboutForm", "Графики курсов валют - О программе"))
        self.text_browser.setHtml(_translate("AboutForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">О программе</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Автор: </span><span style=\" font-size:12pt;\">Никитин Богдан Петрович</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Разработано в качестве проекта для образовательной площадки </span><span style=\" font-size:10pt; font-weight:600; color:#ff0000;\">Я</span><span style=\" font-size:10pt; font-weight:600;\">ндекс </span><span style=\" font-size:10pt;\">Лицей.</span></p></body></html>"))
