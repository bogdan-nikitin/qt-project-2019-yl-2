# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIs/HelpFormUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_HelpForm(object):
    def setupUi(self, HelpForm):
        HelpForm.setObjectName("HelpForm")
        HelpForm.resize(807, 522)
        self.verticalLayout = QtWidgets.QVBoxLayout(HelpForm)
        self.verticalLayout.setObjectName("verticalLayout")
        self.text_browser = QtWidgets.QTextBrowser(HelpForm)
        self.text_browser.setStyleSheet("QTextBrowser{background-color: rgba(0, 0, 0, 0)}")
        self.text_browser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.text_browser.setObjectName("text_browser")
        self.verticalLayout.addWidget(self.text_browser)

        self.retranslateUi(HelpForm)
        QtCore.QMetaObject.connectSlotsByName(HelpForm)

    def retranslateUi(self, HelpForm):
        _translate = QtCore.QCoreApplication.translate
        HelpForm.setWindowTitle(_translate("HelpForm", "Графики курсов валют - Помощь"))
        self.text_browser.setHtml(_translate("HelpForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">Помощь</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">Интерфейс программы</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Строка меню</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">В верхней части окна расположена строка меню со вкладками &quot;Вид&quot; и &quot;Справка&quot;.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Вкладка &quot;Вид&quot; содержит в себе пункт &quot;Перекрестие&quot; отвечающий за переключение состояния перекрестия. Если рядом с пунктом &quot;Перекрестие&quot; стоит галочка(&quot;</span><span style=\" font-family:\'Source Code Pro\'; font-size:8pt; color:#000000;\">✓&quot;), то это означает, что перекрестие включено. Если рядом галочка не установлена, то это говорит о том, что перекрестие выключено.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Source Code Pro\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Source Code Pro\'; font-size:8pt; color:#000000;\">Вкладка &quot;Справка&quot; содержит пункт &quot;Помощь&quot;, при нажатии на который вызывается данное окно, и пункт &quot;О программе&quot;, при нажатии на который всплывает окно с информацией о программе.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Source Code Pro\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Source Code Pro\'; font-size:10pt; font-weight:600; color:#000000;\">Меню вкладок</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Source Code Pro\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Source Code Pro\'; font-size:8pt; color:#000000;\">Ниже строки меню расположена область со вкладками программы. Для добавления новой вкладки нажмите на значок &quot;+&quot;, расположенный после последней вкладки (после вкладки, расположенной правее всех). Для закрытия вкладки нажмите на значок крестика (&quot;x&quot;) в верхнем правом углу открытой вкладки.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Source Code Pro\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Source Code Pro\'; font-size:10pt; font-weight:600; color:#000000;\">Вкладки</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Source Code Pro\'; font-size:10pt; font-weight:600; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Source Code Pro\'; font-size:8pt; color:#000000;\">Все вкладки программы содержат в себе следующие элементы:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Source Code Pro\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Source Code Pro\'; font-size:8pt; color:#000000;\">1. Название валютной пары</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Source Code Pro\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Source Code Pro\'; font-size:8pt; color:#000000;\">2. Кнопка с крестиком, закрывающая вкладку при нажатии.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Source Code Pro\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Source Code Pro\'; font-size:8pt; color:#000000;\">3. Коды ISO валютной пары</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Source Code Pro\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Source Code Pro\'; font-size:8pt; color:#000000;\">4. Текущий курс валютной пары</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Source Code Pro\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Source Code Pro\'; font-size:8pt; color:#000000;\">5. Изменение курса в единицах и в процентах за последний промежуток времени (как правило, за последний день), а также треугольник, направленный вверх, если курс увеличился, и направленный вниз, если курс уменьшился. Если курс не изменился, треугольник не появляется. Цвет надписи зависит от изменения курса: при увелечении курса цвет надписи зелёный, при уменьшении - красный, без изменений - чёрный.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Source Code Pro\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Source Code Pro\'; font-size:8pt; color:#000000;\">6. Выпадающее меню с поиском, в котором можно выбрать валютную пару. Название валютной пары можно вводить с клавиатуры (в этом случае появляется список возможных названий валютных пар, навигацию по которому можно осуществлять с помощью стрелок на клавиатуре). Для подтверждения введённого курса необходимо нажать кнопку &quot;Ввод&quot; (&quot;Enter&quot;).</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Source Code Pro\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Source Code Pro\'; font-size:8pt; color:#000000;\">7. Курс и дата, на которое указывает перекрестие, если оно включено</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Source Code Pro\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Source Code Pro\'; font-size:8pt; color:#000000;\">8. Окно с графиком курса валют. Навигация по графику осуществляется с помощью мыши: удержание левой кнопки мыши и перемещение курсора позволяет перемещаться по графику, кручение колёсика мыши позволяет изменять масштаб графика, правая кнопка мыши вызывает меню настройки графика, удержание правой кнопки мыши и перемещение курсора позволяет растягивать и сжимать график. После смены валютной пары требуется какое-то время на загрузку графика. </span><span style=\" font-family:\'Source Code Pro\'; font-size:8pt; font-weight:600; color:#000000;\">В левом нижнем углу графика расположена кнопка &quot;А&quot;, при нажатии на которую график автоматически масштабируется так, чтобы в область видимости попадал весь график.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Source Code Pro\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Source Code Pro\'; font-size:8pt; color:#000000;\">Элементы расположены в следующем порядке: 1 строка - 1 и 2 элеметы из списка выше, 2 строка - 3, 4, 5 элементы, 3 строка - 6 и 7 элементы, 4 строка - 8 элемент. 1, 3, 4, 5, 6, 8 элементы прижаты к левой стороне окна, 2 и 7 элементы - к правой стороне.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Source Code Pro\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Source Code Pro\'; font-size:11pt; font-weight:600; color:#000000;\">Неисправная работа программы</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Source Code Pro\'; font-size:11pt; font-weight:600; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Source Code Pro\'; font-size:8pt; color:#000000;\">В случае неисправной работы программы(графики курсов валют пустые, программа не запускается, произвольно завершается работа программы) удалите папку &quot;Databases&quot;, находящуюся в одной и той же директории, что и сама программа.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Source Code Pro\'; font-size:8pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Source Code Pro\'; font-size:11pt; font-weight:600; color:#000000;\">Информация о курсах валют</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Source Code Pro\'; font-size:11pt; font-weight:600; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Source Code Pro\'; font-size:8pt; color:#000000;\">Все курсы валют взяты с сайта </span><a href=\"https://cbr.ru\"><span style=\" font-size:8pt; text-decoration: underline; color:#0000ff;\">https://cbr.ru</span></a><span style=\" font-family:\'Source Code Pro\'; font-size:8pt; color:#000000;\">. Процесс получения котировок описан на странице </span><a href=\"https://cbr.ru/development/SXML/\"><span style=\" font-size:8pt; text-decoration: underline; color:#0000ff;\">https://cbr.ru/development/SXML/</span></a><span style=\" font-family:\'Source Code Pro\'; font-size:8pt; color:#000000;\">.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt; text-decoration: underline; color:#000000;\"><br /></p></body></html>"))
