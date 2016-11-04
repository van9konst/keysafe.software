# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QtUserInterfaces/delete_keys.ui'
#
# Created: Fri Nov  4 11:50:10 2016
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

class Ui_DeleteKeys(object):
    def setupUi(self, DeleteKeys):
        DeleteKeys.setObjectName(_fromUtf8("DeleteKeys"))
        DeleteKeys.resize(640, 480)
        self.delete_keys_widget = QtGui.QWidget(DeleteKeys)
        self.delete_keys_widget.setObjectName(_fromUtf8("delete_keys_widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.delete_keys_widget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.delete_key_skroll_area = QtGui.QScrollArea(self.delete_keys_widget)
        self.delete_key_skroll_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.delete_key_skroll_area.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.delete_key_skroll_area.setWidgetResizable(True)
        self.delete_key_skroll_area.setObjectName(_fromUtf8("delete_key_skroll_area"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 607, 386))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.gridLayout_2 = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.delete_key_skroll_area.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.delete_key_skroll_area)
        self.navigate_get_key_menu = QtGui.QGroupBox(self.delete_keys_widget)
        self.navigate_get_key_menu.setTitle(_fromUtf8(""))
        self.navigate_get_key_menu.setCheckable(False)
        self.navigate_get_key_menu.setObjectName(_fromUtf8("navigate_get_key_menu"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.navigate_get_key_menu)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.exit_to_main = QtGui.QPushButton(self.navigate_get_key_menu)
        self.exit_to_main.setStyleSheet(_fromUtf8("font: 75 20pt \"DejaVu Sans Mono for Powerline\";"))
        self.exit_to_main.setObjectName(_fromUtf8("exit_to_main"))
        self.horizontalLayout.addWidget(self.exit_to_main)
        self.verticalLayout.addWidget(self.navigate_get_key_menu)
        DeleteKeys.setCentralWidget(self.delete_keys_widget)
        self.retranslateUi(DeleteKeys)
        QtCore.QMetaObject.connectSlotsByName(DeleteKeys)

    def retranslateUi(self, DeleteKeys):
        DeleteKeys.setWindowTitle(_translate("DeleteKeys", "MainWindow", None))
        self.exit_to_main.setText(_translate("DeleteKeys", "НАЗАД", None))

