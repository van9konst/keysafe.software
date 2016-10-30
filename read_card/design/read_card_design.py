# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QtUserInterfaces/read_card_window.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
#
import math, sys
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import Qt, QTimer
from PyQt4.QtGui import *

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


class Overlay(QWidget):

    def __init__(self, parent = None):

        QWidget.__init__(self, parent)
        palette = QPalette(self.palette())
        palette.setColor(palette.Background, Qt.transparent)
        self.setPalette(palette)

    def paintEvent(self, event):

        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.fillRect(event.rect(), QBrush(QColor(255, 255, 255, 127)))
        painter.setPen(QPen(Qt.NoPen))

        for i in range(6):
            if (self.counter / 5) % 6 == i:
                painter.setBrush(QBrush(QColor(127 + (self.counter % 5)*32, 127, 127)))
            else:
                painter.setBrush(QBrush(QColor(127, 127, 127)))
            painter.drawEllipse(
                self.width()/2 + 30 * math.cos(2 * math.pi * i / 6.0) - 10,
                self.height()/2 + 30 * math.sin(2 * math.pi * i / 6.0) - 10,
                20, 20)

        painter.end()

    def showEvent(self, event):

        self.timer = self.startTimer(50)
        self.counter = 0

    def timerEvent(self, event):

        self.counter += 1
        self.update()
        if self.counter == 200:
            self.killTimer(self.timer)
            self.hide()

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
        self.verticalLayout.addWidget(self.horizontalGroupBox)
        ReadKeyWindow.setCentralWidget(self.ReadKeyFormWidget)

        self.retranslateUi(ReadKeyWindow)
        QtCore.QMetaObject.connectSlotsByName(ReadKeyWindow)

        self.setCentralWidget(self.ReadKeyFormWidget)
        self.overlay = Overlay(self.centralWidget())
        self.overlay.show()


    def resizeEvent(self, event):
        self.overlay.resize(event.size())
        event.accept()

    def retranslateUi(self, ReadKeyWindow):
        ReadKeyWindow.setWindowTitle(_translate("ReadKeyWindow", "MainWindow", None))
        self.label_text.setText(_translate("ReadKeyWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600;\">ПІДНЕСІТЬ </span></p><p align=\"center\"><span style=\" font-size:24pt; font-weight:600;\">СВОЮ КАРТУ </span></p><p align=\"center\"><span style=\" font-size:24pt; font-weight:600;\">ДЛЯ ЗЧИТУВАННЯ</span></p></body></html>", None))
