# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore

from design import get_key_design
from admin_form.admin_form_model import AdminForm
from choice_window.choice_model import ChoiceWindow


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


class GetKeyWindow(QtGui.QMainWindow, get_key_design.Ui_GetKeyWindow):
    def __init__(self, buttons_count):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.exit_to_main.clicked.connect(self.exit)
        self.adminForm = AdminForm()
        self.admin_settings_button.clicked.connect(self.open_settings_menu)
        self.click = None
        if buttons_count:
            buttons = {}
            row_count = 0
            for i in range(buttons_count):
                buttons[i] = QtGui.QPushButton(self.scrollAreaWidgetContents)
                buttons[i].setFixedSize(150, 100)
                buttons[i].setStyleSheet(_fromUtf8("background-color: #669900; font: 75 25pt \"DejaVu Sans Mono for Powerline\";"))
                buttons[i].setText(_translate("GetKeyWindow", str(i), None))
                buttons[i].setObjectName(str(i))
                buttons[i].clicked.connect(self.button_clicked)
                self.gridLayout_2.addWidget(buttons[i], int(row_count % 3), int(row_count / 3))
                row_count += 1

    def button_clicked(self):
        sender = self.sender()
        # need send to 'YES' button object and return key from this method
        self.choice = ChoiceWindow(label_text='Are you sure want to ge key from room {} ?'.format(sender.objectName()))
        self.choice.show()
        QtCore.QTimer.singleShot(5000, self.choice.close)
        print sender.objectName(), ' was pressed'


    def exit(self):
        self.close()

    def open_settings_menu(self):
        self.adminForm.show()

