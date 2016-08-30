# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QtUserInterfaces/admin_form.ui'
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

class Ui_AdminFormMain(object):
    def setupUi(self, AdminFormMain):
        AdminFormMain.setObjectName(_fromUtf8("AdminFormMain"))
        AdminFormMain.resize(640, 480)
        self.settings_menu = QtGui.QWidget(AdminFormMain)
        self.settings_menu.setStyleSheet(_fromUtf8("font: 75 20pt \"DejaVu Sans Mono for Powerline\";"))
        self.settings_menu.setObjectName(_fromUtf8("settings_menu"))
        self.gridLayout = QtGui.QGridLayout(self.settings_menu)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.access_settings = QtGui.QGroupBox(self.settings_menu)
        self.access_settings.setStyleSheet(_fromUtf8("font: 75 20pt \"DejaVu Sans Mono for Powerline\";"))
        self.access_settings.setObjectName(_fromUtf8("access_settings"))
        self.verticalLayout = QtGui.QVBoxLayout(self.access_settings)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.add_new_card = QtGui.QPushButton(self.access_settings)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_new_card.sizePolicy().hasHeightForWidth())
        self.add_new_card.setSizePolicy(sizePolicy)
        self.add_new_card.setStyleSheet(_fromUtf8("color:  rgb(145, 255, 20)"))
        self.add_new_card.setObjectName(_fromUtf8("add_new_card"))
        self.verticalLayout.addWidget(self.add_new_card)
        self.delete_card = QtGui.QPushButton(self.access_settings)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delete_card.sizePolicy().hasHeightForWidth())
        self.delete_card.setSizePolicy(sizePolicy)
        self.delete_card.setStyleSheet(_fromUtf8("color: rgb(255, 67, 1)"))
        self.delete_card.setObjectName(_fromUtf8("delete_card"))
        self.verticalLayout.addWidget(self.delete_card)
        self.set_credentials = QtGui.QPushButton(self.access_settings)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.set_credentials.sizePolicy().hasHeightForWidth())
        self.set_credentials.setSizePolicy(sizePolicy)
        self.set_credentials.setObjectName(_fromUtf8("set_credentials"))
        self.verticalLayout.addWidget(self.set_credentials)
        self.gridLayout.addWidget(self.access_settings, 0, 1, 1, 1)
        self.keys_settings = QtGui.QGroupBox(self.settings_menu)
        self.keys_settings.setObjectName(_fromUtf8("keys_settings"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.keys_settings)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.add_new_key = QtGui.QPushButton(self.keys_settings)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_new_key.sizePolicy().hasHeightForWidth())
        self.add_new_key.setSizePolicy(sizePolicy)
        self.add_new_key.setObjectName(_fromUtf8("add_new_key"))
        self.verticalLayout_2.addWidget(self.add_new_key)
        self.delete_key = QtGui.QPushButton(self.keys_settings)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delete_key.sizePolicy().hasHeightForWidth())
        self.delete_key.setSizePolicy(sizePolicy)
        self.delete_key.setObjectName(_fromUtf8("delete_key"))
        self.verticalLayout_2.addWidget(self.delete_key)
        self.gridLayout.addWidget(self.keys_settings, 0, 2, 1, 1)
        self.exit_to_main = QtGui.QPushButton(self.settings_menu)
        self.exit_to_main.setObjectName(_fromUtf8("exit_to_main"))
        self.gridLayout.addWidget(self.exit_to_main, 1, 2, 1, 1)
        AdminFormMain.setCentralWidget(self.settings_menu)

        self.retranslateUi(AdminFormMain)
        QtCore.QMetaObject.connectSlotsByName(AdminFormMain)

    def retranslateUi(self, AdminFormMain):
        AdminFormMain.setWindowTitle(_translate("AdminFormMain", "MainWindow", None))
        self.access_settings.setTitle(_translate("AdminFormMain", "КЕРУВАННЯ ДОСТУПОМ", None))
        self.add_new_card.setText(_translate("AdminFormMain", "ДОДАТИ НОВУ КАРТУ\n"
" КОРИСТУВАЧА", None))
        self.delete_card.setText(_translate("AdminFormMain", "ВИДАЛИТИ КАРТУ \n"
"КОРИСТУВАЧА", None))
        self.set_credentials.setText(_translate("AdminFormMain", "ВСТАНОВИТИ \n"
"ПРИВІЛЕГІЇ \n"
"ДОСТУПУ", None))
        self.keys_settings.setTitle(_translate("AdminFormMain", "КЕРУВАННЯ КЛЮЧАМИ", None))
        self.add_new_key.setText(_translate("AdminFormMain", "ДОДАТИ НОВИЙ КЛЮЧ", None))
        self.delete_key.setText(_translate("AdminFormMain", "ВИДАЛИТИ КЛЮЧ З СИСТЕМИ", None))
        self.exit_to_main.setText(_translate("AdminFormMain", "ВИХІД", None))

