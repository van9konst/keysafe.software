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


class Ui_ChoiceWindow(object):
    def setupUi(self, ChoiceWindow):
        ChoiceWindow.setObjectName(_fromUtf8("ChoiceWindow"))
        ChoiceWindow.resize(640, 480)
        self.ChoiceFormWidget = QtGui.QWidget(ChoiceWindow)
        self.ChoiceFormWidget.setObjectName(_fromUtf8("ChoiceFormWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.ChoiceFormWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalGroupBox = QtGui.QGroupBox(self.ChoiceFormWidget)
        self.horizontalGroupBox.setObjectName(_fromUtf8("horizontalGroupBox"))
        self.label = QtGui.QLabel(self.horizontalGroupBox)
        self.label.setGeometry(QtCore.QRect(15, 50, 550, 150))
        self.label.setObjectName(_fromUtf8("label"))
        self.yes = QtGui.QPushButton(self.horizontalGroupBox)
        self.yes.setGeometry(QtCore.QRect(0, 230, 291, 201))
        self.yes.setObjectName(_fromUtf8("pushButton"))
        self.no = QtGui.QPushButton(self.horizontalGroupBox)
        self.no.setGeometry(QtCore.QRect(330, 230, 291, 201))
        self.no.setObjectName(_fromUtf8("pushButton_2"))
        self.verticalLayout.addWidget(self.horizontalGroupBox)
        ChoiceWindow.setCentralWidget(self.ChoiceFormWidget)

        self.retranslateUi(ChoiceWindow)
        QtCore.QMetaObject.connectSlotsByName(ChoiceWindow)

    def retranslateUi(self, ChoiceWindow):
        ChoiceWindow.setWindowTitle(_translate("ChoiceWindow", "MainWindow", None))
        self.yes.setText(_translate("ChoiceWindow", "ТАК", None))
        self.no.setText(_translate("ChoiceWindow", "НІ", None))
        self.yes.setStyleSheet('QPushButton {background-color: #ffffff; color: #000000;'
                               'font: 75 50pt DejaVu Sans Mono for Powerline;}')
        self.no.setStyleSheet('QPushButton {background-color: #ffffff; color: #000000;'
                               'font: 75 50pt DejaVu Sans Mono for Powerline;}')