# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../../QtUserInterfaces/chooise_window.ui'
#
# Created: Mon Sep 26 10:28:33 2016
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_ChooiceWindow(object):
    def setupUi(self, ChooiceWindow):
        ChooiceWindow.setObjectName(_fromUtf8("ChooiceWindow"))
        ChooiceWindow.resize(640, 480)
        self.ChooiceFormWidget = QtGui.QWidget(ChooiceWindow)
        self.ChooiceFormWidget.setObjectName(_fromUtf8("ChooiceFormWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.ChooiceFormWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalGroupBox = QtGui.QGroupBox(self.ChooiceFormWidget)
        self.horizontalGroupBox.setObjectName(_fromUtf8("horizontalGroupBox"))
        self.label = QtGui.QLabel(self.horizontalGroupBox)
        self.label.setGeometry(QtCore.QRect(110, 50, 381, 151))
        self.label.setObjectName(_fromUtf8("label"))
        self.yes = QtGui.QPushButton(self.horizontalGroupBox)
        self.yes.setGeometry(QtCore.QRect(0, 230, 291, 201))
        self.yes.setObjectName(_fromUtf8("pushButton"))
        self.no = QtGui.QPushButton(self.horizontalGroupBox)
        self.no.setGeometry(QtCore.QRect(330, 230, 291, 201))
        self.no.setObjectName(_fromUtf8("pushButton_2"))
        self.verticalLayout.addWidget(self.horizontalGroupBox)
        ChooiceWindow.setCentralWidget(self.ChooiceFormWidget)

        self.retranslateUi(ChooiceWindow)
        QtCore.QMetaObject.connectSlotsByName(ChooiceWindow)

    def retranslateUi(self, ChooiceWindow):
        ChooiceWindow.setWindowTitle(_translate("ChooiceWindow", "MainWindow", None))
        self.label.setText(_translate("ChooiceWindow", "<html><head/>\n"
"<body>\n"
"<p align=\"center\">\n"
"<span style=\" font-size:24pt; font-weight:600;\">ТЕКСТ</span>\n"
"</p>\n"
"<p align=\"center\">\n"
"<span style=\" font-size:24pt; font-weight:600;\">name</span>\n"
"</p>\n"
"</body></html>", None))
        self.yes.setText(_translate("ChooiceWindow", "ТАК", None))
        self.no.setText(_translate("ChooiceWindow", "НІ", None))
