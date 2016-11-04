# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QtUserInterfaces/info_window.ui'
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

class Ui_InfoWindow(object):
    def setupUi(self, InfoWindow):
        InfoWindow.setObjectName(_fromUtf8("InfoWindow"))
        InfoWindow.resize(640, 480)
        self.ReadKeyFormWidget = QtGui.QWidget(InfoWindow)
        self.ReadKeyFormWidget.setObjectName(_fromUtf8("ReadKeyFormWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.ReadKeyFormWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalGroupBox = QtGui.QGroupBox(self.ReadKeyFormWidget)
        self.horizontalGroupBox.setObjectName(_fromUtf8("horizontalGroupBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.horizontalGroupBox)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label = QtGui.QLabel(self.horizontalGroupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.button_ok = QtGui.QPushButton(self.horizontalGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_ok.sizePolicy().hasHeightForWidth())
        self.button_ok.setSizePolicy(sizePolicy)
        self.button_ok.setObjectName(_fromUtf8("button_ok"))
        self.verticalLayout_2.addWidget(self.button_ok)
        self.verticalLayout.addWidget(self.horizontalGroupBox)
        InfoWindow.setCentralWidget(self.ReadKeyFormWidget)

        self.retranslateUi(InfoWindow)
        QtCore.QMetaObject.connectSlotsByName(InfoWindow)

    def retranslateUi(self, InfoWindow):
        InfoWindow.setWindowTitle(_translate("InfoWindow", "MainWindow", None))
        self.button_ok.setText(_translate("InfoWindow", "OK", None))
        self.button_ok.setStyleSheet('QPushButton {background-color: #ffffff; color: #000000;'
                                     'font: 75 50pt DejaVu Sans Mono for Powerline;}')

