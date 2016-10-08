# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QtUserInterfaces/add_new_user.ui'
#
# Created: Sat Oct  8 18:06:59 2016
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

class Ui_AddUserWindow(object):
    def setupUi(self, AddUserWindow):
        AddUserWindow.setObjectName(_fromUtf8("AddUserWindow"))
        AddUserWindow.resize(640, 480)
        self.add_user_widget = QtGui.QWidget(AddUserWindow)
        self.add_user_widget.setObjectName(_fromUtf8("add_user_widget"))
        self.new_user_griup_box = QtGui.QGroupBox(self.add_user_widget)
        self.new_user_griup_box.setGeometry(QtCore.QRect(10, 0, 622, 462))
        self.new_user_griup_box.setObjectName(_fromUtf8("new_user_griup_box"))
        self.admin_checkbox = QtGui.QCheckBox(self.new_user_griup_box)
        self.admin_checkbox.setGeometry(QtCore.QRect(60, 170, 431, 41))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.admin_checkbox.sizePolicy().hasHeightForWidth())
        self.admin_checkbox.setSizePolicy(sizePolicy)
        self.admin_checkbox.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("DejaVu Sans Mono for Powerline"))
        font.setPointSize(18)
        self.admin_checkbox.setFont(font)
        self.admin_checkbox.setText(_fromUtf8("ЗРОБИТИ КОРИСТУВАЧА АДМІНІСТРАТОРОМ"))
        self.admin_checkbox.setChecked(False)
        self.admin_checkbox.setAutoRepeat(False)
        self.admin_checkbox.setTristate(False)
        self.admin_checkbox.setObjectName(_fromUtf8("admin_checkbox"))
        self.splitter_4 = QtGui.QSplitter(self.new_user_griup_box)
        self.splitter_4.setGeometry(QtCore.QRect(10, 310, 611, 141))
        self.splitter_4.setOrientation(QtCore.Qt.Vertical)
        self.splitter_4.setObjectName(_fromUtf8("splitter_4"))
        self.add_new_user = QtGui.QPushButton(self.splitter_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_new_user.sizePolicy().hasHeightForWidth())
        self.add_new_user.setSizePolicy(sizePolicy)
        self.add_new_user.setStyleSheet(_fromUtf8("font: 75 20pt \"DejaVu Sans Mono for Powerline\";"))
        self.add_new_user.setObjectName(_fromUtf8("add_new_user"))
        self.pushButton = QtGui.QPushButton(self.splitter_4)
        self.pushButton.setStyleSheet(_fromUtf8("font: 75 20pt \"DejaVu Sans Mono for Powerline\";"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.splitter_3 = QtGui.QSplitter(self.new_user_griup_box)
        self.splitter_3.setGeometry(QtCore.QRect(10, 240, 581, 41))
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName(_fromUtf8("splitter_3"))
        self.rfid = QtGui.QPlainTextEdit(self.splitter_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rfid.sizePolicy().hasHeightForWidth())
        self.rfid.setSizePolicy(sizePolicy)
        self.rfid.setObjectName(_fromUtf8("rfid"))
        self.add_card_for_new_user = QtGui.QPushButton(self.splitter_3)
        self.add_card_for_new_user.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_card_for_new_user.sizePolicy().hasHeightForWidth())
        self.add_card_for_new_user.setSizePolicy(sizePolicy)
        self.add_card_for_new_user.setStyleSheet(_fromUtf8("font: 75 20pt \"DejaVu Sans Mono for Powerline\";"))
        self.add_card_for_new_user.setObjectName(_fromUtf8("add_card_for_new_user"))
        self.splitter = QtGui.QSplitter(self.new_user_griup_box)
        self.splitter.setGeometry(QtCore.QRect(20, 30, 571, 51))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.lineEdit_firstname = QtGui.QLineEdit(self.splitter)
        self.lineEdit_firstname.setObjectName(_fromUtf8("lineEdit_firstname"))
        self.label = QtGui.QLabel(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("DejaVu Sans Mono for Powerline"))
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.splitter_2 = QtGui.QSplitter(self.new_user_griup_box)
        self.splitter_2.setGeometry(QtCore.QRect(20, 90, 561, 61))
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.lineEdit_lastname = QtGui.QLineEdit(self.splitter_2)
        self.lineEdit_lastname.setObjectName(_fromUtf8("lineEdit_lastname"))
        self.label_2 = QtGui.QLabel(self.splitter_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Sans Mono for Powerline"))
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        AddUserWindow.setCentralWidget(self.add_user_widget)

        self.retranslateUi(AddUserWindow)
        QtCore.QMetaObject.connectSlotsByName(AddUserWindow)

    def retranslateUi(self, AddUserWindow):
        AddUserWindow.setWindowTitle(_translate("AddUserWindow", "MainWindow", None))
        self.add_new_user.setText(_translate("AddUserWindow", "ДОДАТИ", None))
        self.pushButton.setText(_translate("AddUserWindow", "НАЗАД", None))
        self.add_card_for_new_user.setText(_translate("AddUserWindow", "ПРИКРІПИТИ КЛЮЧ-КАРТУ", None))
        self.label.setText(_translate("AddUserWindow", "Імя", None))
        self.label_2.setText(_translate("AddUserWindow", "Прізвище", None))

