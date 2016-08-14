# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QtUserInterfaces/add_new_user.ui'
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

class Ui_AddUserWindow(object):
    def setupUi(self, AddUserWindow):
        AddUserWindow.setObjectName(_fromUtf8("AddUserWindow"))
        AddUserWindow.resize(640, 480)
        self.add_user_widget = QtGui.QWidget(AddUserWindow)
        self.add_user_widget.setObjectName(_fromUtf8("add_user_widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.add_user_widget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.new_user_griup_box = QtGui.QGroupBox(self.add_user_widget)
        self.new_user_griup_box.setObjectName(_fromUtf8("new_user_griup_box"))
        self.gridLayout = QtGui.QGridLayout(self.new_user_griup_box)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.edit_name = QtGui.QPushButton(self.new_user_griup_box)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edit_name.sizePolicy().hasHeightForWidth())
        self.edit_name.setSizePolicy(sizePolicy)
        self.edit_name.setStyleSheet(_fromUtf8("font: 75 20pt \"DejaVu Sans Mono for Powerline\";"))
        self.edit_name.setObjectName(_fromUtf8("edit_name"))
        self.gridLayout.addWidget(self.edit_name, 0, 1, 1, 1)
        self.name = QtGui.QLineEdit(self.new_user_griup_box)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name.sizePolicy().hasHeightForWidth())
        self.name.setSizePolicy(sizePolicy)
        self.name.setStyleSheet(_fromUtf8("font: 75 20pt \"DejaVu Sans Mono for Powerline\";"))
        self.name.setObjectName(_fromUtf8("name"))
        self.gridLayout.addWidget(self.name, 0, 0, 1, 1)
        self.add_card_for_new_user = QtGui.QPushButton(self.new_user_griup_box)
        self.add_card_for_new_user.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_card_for_new_user.sizePolicy().hasHeightForWidth())
        self.add_card_for_new_user.setSizePolicy(sizePolicy)
        self.add_card_for_new_user.setStyleSheet(_fromUtf8("font: 75 20pt \"DejaVu Sans Mono for Powerline\";"))
        self.add_card_for_new_user.setObjectName(_fromUtf8("add_card_for_new_user"))
        self.gridLayout.addWidget(self.add_card_for_new_user, 5, 0, 1, 2)
        self.add_new_user = QtGui.QPushButton(self.new_user_griup_box)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_new_user.sizePolicy().hasHeightForWidth())
        self.add_new_user.setSizePolicy(sizePolicy)
        self.add_new_user.setStyleSheet(_fromUtf8("font: 75 20pt \"DejaVu Sans Mono for Powerline\";"))
        self.add_new_user.setObjectName(_fromUtf8("add_new_user"))
        self.gridLayout.addWidget(self.add_new_user, 6, 0, 1, 2)
        self.verticalLayout.addWidget(self.new_user_griup_box)
        self.pushButton = QtGui.QPushButton(self.add_user_widget)
        self.pushButton.setStyleSheet(_fromUtf8("font: 75 20pt \"DejaVu Sans Mono for Powerline\";"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout.addWidget(self.pushButton)
        AddUserWindow.setCentralWidget(self.add_user_widget)

        self.retranslateUi(AddUserWindow)
        QtCore.QMetaObject.connectSlotsByName(AddUserWindow)

    def retranslateUi(self, AddUserWindow):
        AddUserWindow.setWindowTitle(_translate("AddUserWindow", "MainWindow", None))
        self.edit_name.setText(_translate("AddUserWindow", "РЕДАГУВАТИ", None))
        self.name.setInputMask(_translate("AddUserWindow", "ПЕТРО ПЕТРЕНКО", None))
        self.add_card_for_new_user.setText(_translate("AddUserWindow", "ПРИКРІПИТИ КЛЮЧ-КАРТУ", None))
        self.add_new_user.setText(_translate("AddUserWindow", "ДОДАТИ", None))
        self.pushButton.setText(_translate("AddUserWindow", "НАЗАД", None))

