# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QtUserInterfaces/add_new_room.ui'
#
# Created: Wed Nov  2 16:28:52 2016
#      by: PyQt4 UI code generator 4.10.4
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

class Ui_addRoomWindow(object):
    def setupUi(self, addRoomWindow):
        addRoomWindow.setObjectName(_fromUtf8("addRoomWindow"))
        addRoomWindow.resize(640, 480)
        self.add_user_widget = QtGui.QWidget(addRoomWindow)
        self.add_user_widget.setObjectName(_fromUtf8("add_user_widget"))
        self.splitter = QtGui.QSplitter(self.add_user_widget)
        self.splitter.setGeometry(QtCore.QRect(10, 10, 621, 451))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.widget = QtGui.QWidget(self.splitter)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.rfid_chip = QtGui.QLineEdit(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rfid_chip.sizePolicy().hasHeightForWidth())
        self.rfid_chip.setSizePolicy(sizePolicy)
        self.rfid_chip.setStyleSheet(_fromUtf8("font: 75 20pt \"DejaVu Sans Mono for Powerline\";"))
        self.rfid_chip.setObjectName(_fromUtf8("rfid_chip"))
        self.gridLayout.addWidget(self.rfid_chip, 1, 1, 1, 1)
        self.add_rfid_chip = QtGui.QPushButton(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_rfid_chip.sizePolicy().hasHeightForWidth())
        self.add_rfid_chip.setSizePolicy(sizePolicy)
        self.add_rfid_chip.setStyleSheet(_fromUtf8("font: 75 20pt \"DejaVu Sans Mono for Powerline\";"))
        self.add_rfid_chip.setObjectName(_fromUtf8("add_rfid_chip"))
        self.gridLayout.addWidget(self.add_rfid_chip, 1, 0, 1, 1)
        self.room = QtGui.QLineEdit(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.room.sizePolicy().hasHeightForWidth())
        self.room.setSizePolicy(sizePolicy)
        self.room.setStyleSheet(_fromUtf8("font: 75 20pt \"DejaVu Sans Mono for Powerline\";"))
        self.room.setObjectName(_fromUtf8("room"))
        self.gridLayout.addWidget(self.room, 0, 1, 1, 1)
        self.room_label = QtGui.QLabel(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.room_label.sizePolicy().hasHeightForWidth())
        self.room_label.setSizePolicy(sizePolicy)
        self.room_label.setStyleSheet(_fromUtf8("font: 75 20pt \"DejaVu Sans Mono for Powerline\";"))
        self.room_label.setObjectName(_fromUtf8("room_label"))
        self.gridLayout.addWidget(self.room_label, 0, 0, 1, 1)
        self.widget1 = QtGui.QWidget(self.splitter)
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget1)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.add_new_key = QtGui.QPushButton(self.widget1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_new_key.sizePolicy().hasHeightForWidth())
        self.add_new_key.setSizePolicy(sizePolicy)
        self.add_new_key.setStyleSheet(_fromUtf8("font: 75 20pt \"DejaVu Sans Mono for Powerline\";"))
        self.add_new_key.setObjectName(_fromUtf8("add_new_key"))
        self.horizontalLayout.addWidget(self.add_new_key)
        self.exit_to_main = QtGui.QPushButton(self.widget1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exit_to_main.sizePolicy().hasHeightForWidth())
        self.exit_to_main.setSizePolicy(sizePolicy)
        self.exit_to_main.setStyleSheet(_fromUtf8("font: 75 20pt \"DejaVu Sans Mono for Powerline\";"))
        self.exit_to_main.setObjectName(_fromUtf8("exit_to_main"))
        self.horizontalLayout.addWidget(self.exit_to_main)
        addRoomWindow.setCentralWidget(self.add_user_widget)

        self.retranslateUi(addRoomWindow)
        QtCore.QMetaObject.connectSlotsByName(addRoomWindow)

    def retranslateUi(self, addRoomWindow):
        addRoomWindow.setWindowTitle(_translate("addRoomWindow", "MainWindow", None))
        self.add_rfid_chip.setText(_translate("addRoomWindow", "Прикріпити мітку ключа", None))
        self.room_label.setText(_translate("addRoomWindow", "Кімната", None))
        self.add_new_key.setText(_translate("addRoomWindow", "Додати ", None))
        self.exit_to_main.setText(_translate("addRoomWindow", "Вихід", None))

