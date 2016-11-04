# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QtUserInterfaces/delete_users.ui'
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

class Ui_DeleteUsers(object):
    def setupUi(self, DeleteUsers):
        DeleteUsers.setObjectName(_fromUtf8("DeleteUsers"))
        DeleteUsers.resize(640, 480)
        self.delete_users_widget = QtGui.QWidget(DeleteUsers)
        self.delete_users_widget.setObjectName(_fromUtf8("delete_users_widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.delete_users_widget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.delete_user_skroll_area = QtGui.QScrollArea(self.delete_users_widget)
        self.delete_user_skroll_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.delete_user_skroll_area.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.delete_user_skroll_area.setWidgetResizable(True)
        self.delete_user_skroll_area.setObjectName(_fromUtf8("delete_user_skroll_area"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 607, 386))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.gridLayout_2 = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.pushButton_17 = QtGui.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_17.sizePolicy().hasHeightForWidth())
        self.pushButton_17.setSizePolicy(sizePolicy)
        self.pushButton_17.setStyleSheet(_fromUtf8("font: 75 20pt \"DejaVu Sans Mono for Powerline\";"))
        self.pushButton_17.setObjectName(_fromUtf8("pushButton_17"))
        self.gridLayout_2.addWidget(self.pushButton_17, 1, 0, 1, 1)
        self.pushButton_7 = QtGui.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        self.pushButton_7.setStyleSheet(_fromUtf8("font: 75 20pt \"DejaVu Sans Mono for Powerline\";"))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.gridLayout_2.addWidget(self.pushButton_7, 1, 2, 1, 1)
        self.pushButton_15 = QtGui.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_15.sizePolicy().hasHeightForWidth())
        self.pushButton_15.setSizePolicy(sizePolicy)
        self.pushButton_15.setStyleSheet(_fromUtf8("font: 75 20pt \"DejaVu Sans Mono for Powerline\";"))
        self.pushButton_15.setObjectName(_fromUtf8("pushButton_15"))
        self.gridLayout_2.addWidget(self.pushButton_15, 1, 1, 1, 1)
        self.room_button_303 = QtGui.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.room_button_303.sizePolicy().hasHeightForWidth())
        self.room_button_303.setSizePolicy(sizePolicy)
        self.room_button_303.setStyleSheet(_fromUtf8("font: 75 20pt \"DejaVu Sans Mono for Powerline\";"))
        self.room_button_303.setObjectName(_fromUtf8("room_button_303"))
        self.gridLayout_2.addWidget(self.room_button_303, 0, 0, 1, 1)
        self.room_button_302 = QtGui.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.room_button_302.sizePolicy().hasHeightForWidth())
        self.room_button_302.setSizePolicy(sizePolicy)
        self.room_button_302.setStyleSheet(_fromUtf8("font: 75 20pt \"DejaVu Sans Mono for Powerline\";"))
        self.room_button_302.setObjectName(_fromUtf8("room_button_302"))
        self.gridLayout_2.addWidget(self.room_button_302, 0, 2, 1, 1)
        self.room_button_301 = QtGui.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.room_button_301.sizePolicy().hasHeightForWidth())
        self.room_button_301.setSizePolicy(sizePolicy)
        self.room_button_301.setStyleSheet(_fromUtf8("font: 75 20pt \"DejaVu Sans Mono for Powerline\";"))
        self.room_button_301.setObjectName(_fromUtf8("room_button_301"))
        self.gridLayout_2.addWidget(self.room_button_301, 0, 1, 1, 1)
        self.delete_user_skroll_area.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.delete_user_skroll_area)
        self.navigate_get_key_menu = QtGui.QGroupBox(self.delete_users_widget)
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
        DeleteUsers.setCentralWidget(self.delete_users_widget)

        self.retranslateUi(DeleteUsers)
        QtCore.QMetaObject.connectSlotsByName(DeleteUsers)

    def retranslateUi(self, DeleteUsers):
        DeleteUsers.setWindowTitle(_translate("DeleteUsers", "MainWindow", None))
        self.pushButton_17.setText(_translate("DeleteUsers", "PushButton", None))
        self.pushButton_7.setText(_translate("DeleteUsers", "PushButton", None))
        self.pushButton_15.setText(_translate("DeleteUsers", "PushButton", None))
        self.room_button_303.setText(_translate("DeleteUsers", "303", None))
        self.room_button_302.setText(_translate("DeleteUsers", "302", None))
        self.room_button_301.setText(_translate("DeleteUsers", "301", None))
        self.exit_to_main.setText(_translate("DeleteUsers", "НАЗАД", None))

