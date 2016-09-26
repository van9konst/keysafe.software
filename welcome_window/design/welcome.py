# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../../QtUserInterfaces/welcome_window.ui'
#
# Created: Mon Sep 26 10:29:40 2016
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

class Ui_WelcomeWindow(object):
    def setupUi(self, WelcomeWindow):
        WelcomeWindow.setObjectName(_fromUtf8("WelcomeWindow"))
        WelcomeWindow.resize(640, 480)
        self.WelcomeFormWidget = QtGui.QWidget(WelcomeWindow)
        self.WelcomeFormWidget.setObjectName(_fromUtf8("WelcomeFormWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.WelcomeFormWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalGroupBox = QtGui.QGroupBox(self.WelcomeFormWidget)
        self.horizontalGroupBox.setObjectName(_fromUtf8("horizontalGroupBox"))
        self.label_text = QtGui.QLabel(self.horizontalGroupBox)
        self.label_text.setGeometry(QtCore.QRect(170, 100, 301, 156))
        self.label_text.setObjectName(_fromUtf8("label_text"))
        self.label = QtGui.QLabel(self.horizontalGroupBox)
        self.label.setGeometry(QtCore.QRect(20, 230, 591, 71))
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.horizontalGroupBox)
        WelcomeWindow.setCentralWidget(self.WelcomeFormWidget)

        self.retranslateUi(WelcomeWindow)
        QtCore.QMetaObject.connectSlotsByName(WelcomeWindow)

    def retranslateUi(self, WelcomeWindow):
        WelcomeWindow.setWindowTitle(_translate("WelcomeWindow", "MainWindow", None))
        self.label_text.setText(_translate("WelcomeWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600;\">ВІТАЮ ! </span></p><p align=\"center\"><span style=\" font-size:24pt; font-weight:600;\">ВИ УВІЙШЛИ ЯК </span></p></body></html>", None))
        self.label.setText(_translate("WelcomeWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600;\">username</span></p></body></html>", None))
