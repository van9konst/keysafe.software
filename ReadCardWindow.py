# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QtUserInterfaces/read_card_window.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_ReadKeyWindow(object):
    def setupUi(self, ReadKeyWindow):
        ReadKeyWindow.setObjectName(_fromUtf8("ReadKeyWindow"))
        ReadKeyWindow.resize(640, 480)
        self.ReadKeyFormWidget = QtGui.QWidget(ReadKeyWindow)
        self.ReadKeyFormWidget.setObjectName(_fromUtf8("ReadKeyFormWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.ReadKeyFormWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalGroupBox = QtGui.QGroupBox(self.ReadKeyFormWidget)
        self.horizontalGroupBox.setObjectName(_fromUtf8("horizontalGroupBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.horizontalGroupBox)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_text = QtGui.QLabel(self.horizontalGroupBox)
        self.label_text.setObjectName(_fromUtf8("label_text"))
        self.verticalLayout_2.addWidget(self.label_text)
        self.progressBar = QtGui.QProgressBar(self.horizontalGroupBox)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.verticalLayout_2.addWidget(self.progressBar)
        self.verticalLayout.addWidget(self.horizontalGroupBox)
        self.exit_to_main = QtGui.QPushButton(self.ReadKeyFormWidget)
        self.exit_to_main.setStyleSheet(_fromUtf8("font: 75 20pt \"DejaVu Sans Mono for Powerline\";"))
        self.exit_to_main.setObjectName(_fromUtf8("exit_to_main"))
        self.verticalLayout.addWidget(self.exit_to_main)
        ReadKeyWindow.setCentralWidget(self.ReadKeyFormWidget)

        self.retranslateUi(ReadKeyWindow)
        QtCore.QMetaObject.connectSlotsByName(ReadKeyWindow)

    def retranslateUi(self, ReadKeyWindow):
        ReadKeyWindow.setWindowTitle(_translate("ReadKeyWindow", "MainWindow", None))
        self.label_text.setText(_translate("ReadKeyWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600;\">ПІДНЕСІТЬ </span></p><p align=\"center\"><span style=\" font-size:24pt; font-weight:600;\">СВОЮ КАРТУ </span></p><p align=\"center\"><span style=\" font-size:24pt; font-weight:600;\">ДЛЯ ЗЧИТУВАННЯ</span></p></body></html>", None))
        self.exit_to_main.setText(_translate("ReadKeyWindow", "ВИХІД", None))

