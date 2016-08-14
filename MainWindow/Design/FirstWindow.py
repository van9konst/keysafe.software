# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QtUserInterfaces/first_window.ui'
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

class Ui_FirstWindow(object):
    def setupUi(self, FirstWindow):
        FirstWindow.setObjectName(_fromUtf8("FirstWindow"))
        FirstWindow.resize(640, 480)
        self.main_menu = QtGui.QWidget(FirstWindow)
        self.main_menu.setObjectName(_fromUtf8("main_menu"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.main_menu)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.get_key = QtGui.QPushButton(self.main_menu)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.get_key.sizePolicy().hasHeightForWidth())
        self.get_key.setSizePolicy(sizePolicy)
        self.get_key.setStyleSheet(_fromUtf8("font: 75 20pt \"DejaVu Sans Mono for Powerline\";"))
        self.get_key.setObjectName(_fromUtf8("get_key"))
        self.horizontalLayout.addWidget(self.get_key)
        self.return_key = QtGui.QPushButton(self.main_menu)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.return_key.sizePolicy().hasHeightForWidth())
        self.return_key.setSizePolicy(sizePolicy)
        self.return_key.setStyleSheet(_fromUtf8("font: 75 20pt \"DejaVu Sans Mono for Powerline\";"))
        self.return_key.setObjectName(_fromUtf8("return_key"))
        self.horizontalLayout.addWidget(self.return_key)
        FirstWindow.setCentralWidget(self.main_menu)

        self.retranslateUi(FirstWindow)
        QtCore.QMetaObject.connectSlotsByName(FirstWindow)

    def retranslateUi(self, FirstWindow):
        FirstWindow.setWindowTitle(_translate("FirstWindow", "MainWindow", None))
        self.get_key.setText(_translate("FirstWindow", "ВЗЯТИ ВКЛЮЧ", None))
        self.return_key.setText(_translate("FirstWindow", "ПОКЛАСТИ КЛЮЧ", None))

