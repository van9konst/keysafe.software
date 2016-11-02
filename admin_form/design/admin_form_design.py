# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QtUserInterfaces/admin_form.ui'
#
# Created: Wed Nov  2 15:00:19 2016
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

class Ui_AdminFormMain(object):
    def setupUi(self, AdminFormMain):
        AdminFormMain.setObjectName(_fromUtf8("AdminFormMain"))
        AdminFormMain.resize(640, 480)
        self.settings_menu = QtGui.QWidget(AdminFormMain)
        self.settings_menu.setStyleSheet(_fromUtf8("font: 75 20pt \"DejaVu Sans Mono for Powerline\";"))
        self.settings_menu.setObjectName(_fromUtf8("settings_menu"))
        self.gridLayout = QtGui.QGridLayout(self.settings_menu)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.users_settings = QtGui.QGroupBox(self.settings_menu)
        self.users_settings.setStyleSheet(_fromUtf8("font: 75 20pt \"DejaVu Sans Mono for Powerline\";"))
        self.users_settings.setObjectName(_fromUtf8("users_settings"))
        self.verticalLayout = QtGui.QVBoxLayout(self.users_settings)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.new_user = QtGui.QPushButton(self.users_settings)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.new_user.sizePolicy().hasHeightForWidth())
        self.new_user.setSizePolicy(sizePolicy)
        self.new_user.setStyleSheet(_fromUtf8(""))
        self.new_user.setObjectName(_fromUtf8("new_user"))
        self.verticalLayout.addWidget(self.new_user)
        self.remove_user = QtGui.QPushButton(self.users_settings)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.remove_user.sizePolicy().hasHeightForWidth())
        self.remove_user.setSizePolicy(sizePolicy)
        self.remove_user.setStyleSheet(_fromUtf8(""))
        self.remove_user.setObjectName(_fromUtf8("remove_user"))
        self.verticalLayout.addWidget(self.remove_user)
        self.gridLayout.addWidget(self.users_settings, 0, 1, 1, 1)
        self.keys_settings = QtGui.QGroupBox(self.settings_menu)
        self.keys_settings.setObjectName(_fromUtf8("keys_settings"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.keys_settings)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.new_key = QtGui.QPushButton(self.keys_settings)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.new_key.sizePolicy().hasHeightForWidth())
        self.new_key.setSizePolicy(sizePolicy)
        self.new_key.setObjectName(_fromUtf8("new_key"))
        self.verticalLayout_2.addWidget(self.new_key)
        self.remove_key = QtGui.QPushButton(self.keys_settings)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.remove_key.sizePolicy().hasHeightForWidth())
        self.remove_key.setSizePolicy(sizePolicy)
        self.remove_key.setObjectName(_fromUtf8("remove_key"))
        self.verticalLayout_2.addWidget(self.remove_key)
        self.gridLayout.addWidget(self.keys_settings, 0, 2, 1, 1)
        self.exit_to_main = QtGui.QPushButton(self.settings_menu)
        self.exit_to_main.setObjectName(_fromUtf8("exit_to_main"))
        self.gridLayout.addWidget(self.exit_to_main, 1, 2, 1, 1)
        AdminFormMain.setCentralWidget(self.settings_menu)

        self.retranslateUi(AdminFormMain)
        QtCore.QMetaObject.connectSlotsByName(AdminFormMain)

    def retranslateUi(self, AdminFormMain):
        AdminFormMain.setWindowTitle(_translate("AdminFormMain", "MainWindow", None))
        self.users_settings.setTitle(_translate("AdminFormMain", "КЕРУВАННЯ КОРИСТУВАЧАМИ", None))
        self.new_user.setText(_translate("AdminFormMain", "ДОДАТИ КОРИСТУВАЧА", None))
        self.remove_user.setText(_translate("AdminFormMain", "ВИДАЛИТИ КОРИСТУВАЧА", None))
        self.keys_settings.setTitle(_translate("AdminFormMain", "КЕРУВАННЯ КЛЮЧАМИ", None))
        self.new_key.setText(_translate("AdminFormMain", "ДОДАТИ КЛЮЧ", None))
        self.remove_key.setText(_translate("AdminFormMain", "ВИДАЛИТИ КЛЮЧ ", None))
        self.exit_to_main.setText(_translate("AdminFormMain", "ВИХІД", None))

