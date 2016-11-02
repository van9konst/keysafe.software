# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QtUserInterfaces/add_new_user.ui'
#
# Created: Wed Nov  2 15:28:10 2016
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
        self.splitter = QtGui.QSplitter(self.add_user_widget)
        self.splitter.setGeometry(QtCore.QRect(10, 10, 621, 451))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.widget = QtGui.QWidget(self.splitter)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.firstname_label = QtGui.QLabel(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.firstname_label.sizePolicy().hasHeightForWidth())
        self.firstname_label.setSizePolicy(sizePolicy)
        self.firstname_label.setStyleSheet(_fromUtf8("font: 75 20pt \"DejaVu Sans Mono for Powerline\";"))
        self.firstname_label.setObjectName(_fromUtf8("firstname_label"))
        self.gridLayout.addWidget(self.firstname_label, 0, 0, 1, 1)
        self.firstname = QtGui.QLineEdit(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.firstname.sizePolicy().hasHeightForWidth())
        self.firstname.setSizePolicy(sizePolicy)
        self.firstname.setStyleSheet(_fromUtf8("font: 75 20pt \"DejaVu Sans Mono for Powerline\";"))
        self.firstname.setObjectName(_fromUtf8("firstname"))
        self.gridLayout.addWidget(self.firstname, 0, 1, 1, 1)
        self.lastname_label = QtGui.QLabel(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lastname_label.sizePolicy().hasHeightForWidth())
        self.lastname_label.setSizePolicy(sizePolicy)
        self.lastname_label.setStyleSheet(_fromUtf8("font: 75 20pt \"DejaVu Sans Mono for Powerline\";"))
        self.lastname_label.setObjectName(_fromUtf8("lastname_label"))
        self.gridLayout.addWidget(self.lastname_label, 1, 0, 1, 1)
        self.lastname = QtGui.QLineEdit(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lastname.sizePolicy().hasHeightForWidth())
        self.lastname.setSizePolicy(sizePolicy)
        self.lastname.setStyleSheet(_fromUtf8("font: 75 20pt \"DejaVu Sans Mono for Powerline\";"))
        self.lastname.setObjectName(_fromUtf8("lastname"))
        self.gridLayout.addWidget(self.lastname, 1, 1, 1, 1)
        self.admin_checkbox = QtGui.QCheckBox(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.admin_checkbox.sizePolicy().hasHeightForWidth())
        self.admin_checkbox.setSizePolicy(sizePolicy)
        self.admin_checkbox.setStyleSheet(_fromUtf8("font: 75 20pt \"DejaVu Sans Mono for Powerline\";"))
        self.admin_checkbox.setObjectName(_fromUtf8("admin_checkbox"))
        self.gridLayout.addWidget(self.admin_checkbox, 2, 1, 1, 1)
        self.add_rfid_card = QtGui.QPushButton(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_rfid_card.sizePolicy().hasHeightForWidth())
        self.add_rfid_card.setSizePolicy(sizePolicy)
        self.add_rfid_card.setStyleSheet(_fromUtf8("font: 75 20pt \"DejaVu Sans Mono for Powerline\";"))
        self.add_rfid_card.setObjectName(_fromUtf8("add_rfid_card"))
        self.gridLayout.addWidget(self.add_rfid_card, 3, 0, 1, 1)
        self.rfid_card = QtGui.QLineEdit(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rfid_card.sizePolicy().hasHeightForWidth())
        self.rfid_card.setSizePolicy(sizePolicy)
        self.rfid_card.setStyleSheet(_fromUtf8("font: 75 20pt \"DejaVu Sans Mono for Powerline\";"))
        self.rfid_card.setObjectName(_fromUtf8("rfid_card"))
        self.gridLayout.addWidget(self.rfid_card, 3, 1, 1, 1)
        self.widget1 = QtGui.QWidget(self.splitter)
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget1)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.add_new_user = QtGui.QPushButton(self.widget1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_new_user.sizePolicy().hasHeightForWidth())
        self.add_new_user.setSizePolicy(sizePolicy)
        self.add_new_user.setStyleSheet(_fromUtf8("font: 75 20pt \"DejaVu Sans Mono for Powerline\";"))
        self.add_new_user.setObjectName(_fromUtf8("add_new_user"))
        self.horizontalLayout.addWidget(self.add_new_user)
        self.exit_to_main = QtGui.QPushButton(self.widget1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exit_to_main.sizePolicy().hasHeightForWidth())
        self.exit_to_main.setSizePolicy(sizePolicy)
        self.exit_to_main.setStyleSheet(_fromUtf8("font: 75 20pt \"DejaVu Sans Mono for Powerline\";"))
        self.exit_to_main.setObjectName(_fromUtf8("exit_to_main"))
        self.horizontalLayout.addWidget(self.exit_to_main)
        AddUserWindow.setCentralWidget(self.add_user_widget)

        self.retranslateUi(AddUserWindow)
        QtCore.QMetaObject.connectSlotsByName(AddUserWindow)

    def retranslateUi(self, AddUserWindow):
        AddUserWindow.setWindowTitle(_translate("AddUserWindow", "MainWindow", None))
        self.firstname_label.setText(_translate("AddUserWindow", "ІМЯ", None))
        self.lastname_label.setText(_translate("AddUserWindow", "ПРІЗВИЩЕ", None))
        self.admin_checkbox.setText(_translate("AddUserWindow", "Зробити користувача адміністратором", None))
        self.add_rfid_card.setText(_translate("AddUserWindow", "Прикріпити карту", None))
        self.add_new_user.setText(_translate("AddUserWindow", "Додати ", None))
        self.exit_to_main.setText(_translate("AddUserWindow", "Вихід", None))

