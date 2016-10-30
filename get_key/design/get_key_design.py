# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QtUserInterfaces/get_key_window.ui'
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

class Ui_GetKeyWindow(object):
    def setupUi(self, GetKeyWindow):
        GetKeyWindow.setObjectName(_fromUtf8("GetKeyWindow"))
        GetKeyWindow.resize(640, 480)
        self.get_key_widget = QtGui.QWidget(GetKeyWindow)
        self.get_key_widget.setObjectName(_fromUtf8("get_key_widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.get_key_widget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.get_key_skroll_area = QtGui.QScrollArea(self.get_key_widget)
        self.get_key_skroll_area.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.get_key_skroll_area.setWidgetResizable(True)
        self.get_key_skroll_area.setObjectName(_fromUtf8("get_key_skroll_area"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 599, 390))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.gridLayout_2 = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.get_key_skroll_area.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.get_key_skroll_area)
        self.navigate_get_key_menu = QtGui.QGroupBox(self.get_key_widget)
        self.navigate_get_key_menu.setTitle(_fromUtf8(""))
        self.navigate_get_key_menu.setCheckable(False)
        self.navigate_get_key_menu.setObjectName(_fromUtf8("navigate_get_key_menu"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.navigate_get_key_menu)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.exit_to_main = QtGui.QPushButton(self.navigate_get_key_menu)
        self.exit_to_main.setStyleSheet(_fromUtf8("font: 75 20pt \"DejaVu Sans Mono for Powerline\";"))
        self.exit_to_main.setObjectName(_fromUtf8("exit_to_main"))
        self.horizontalLayout.addWidget(self.exit_to_main)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.verticalLayout.addWidget(self.navigate_get_key_menu)
        self.admin_settings_button = QtGui.QPushButton(self.get_key_widget)
        self.admin_settings_button.setEnabled(True)
        self.admin_settings_button.setVisible(False)
        self.admin_settings_button.setStyleSheet(_fromUtf8("font: 75 20pt \"DejaVu Sans Mono for Powerline\";"))
        self.admin_settings_button.setObjectName(_fromUtf8("admin_settings_button"))
        self.verticalLayout.addWidget(self.admin_settings_button)
        GetKeyWindow.setCentralWidget(self.get_key_widget)
        self.retranslateUi(GetKeyWindow)
        QtCore.QMetaObject.connectSlotsByName(GetKeyWindow)


    def retranslateUi(self, GetKeyWindow):
        GetKeyWindow.setWindowTitle(_translate("GetKeyWindow", "MainWindow", None))
        self.exit_to_main.setText(_translate("GetKeyWindow", "ВИХІД", None))
        self.admin_settings_button.setText(_translate("GetKeyWindow", "КЕРУВАННЯ", None))

