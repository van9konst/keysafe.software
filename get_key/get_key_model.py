# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore

from design import get_key_design
from admin_form.admin_form_model import AdminForm
from choice_window.choice_model import ChoiceWindow
from database.models import Key, UserKeyLink


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
    def __init__(self, keys, user=None):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.user = user
        self.exit_to_main.clicked.connect(self.exit)
        self.adminForm = AdminForm()
        self.admin_settings_button.clicked.connect(self.open_settings_menu)
        self.click = None
        if keys:
            buttons = {}
            row_count = 0
            for key in keys:
                buttons[key.id] = QtGui.QPushButton(self.scrollAreaWidgetContents)
                buttons[key.id].setFixedSize(150, 100)
                if key.status is True:
                    buttons[key.id].setStyleSheet('QPushButton {background-color: #669900;'
                                                  'color: #ffffff;'
                                                  'font: 75 40pt DejaVu Sans Mono for Powerline;}')
                else:
                    buttons[key.id].setStyleSheet('QPushButton {background-color: #cc3300;'
                                                  'color: #ffffff;'
                                                  'font: 75 40pt DejaVu Sans Mono for Powerline;}')
                buttons[key.id].setText(_translate("GetKeyWindow", str(key.room), None))
                buttons[key.id].setObjectName(key.rfid_s)
                buttons[key.id].clicked.connect(self.button_clicked)
                self.gridLayout_2.addWidget(buttons[key.id], int(row_count % 3), int(row_count / 3))
                row_count += 1

    def button_clicked(self):
        sender = self.sender()
        key = Key.key_get_by_rfid(str(sender.objectName()))
        if key['data']:
            if key['data'].status is True:
                self.choice = ChoiceWindow(
                    label_text=u'Ви дійсно хочете взяти ключ від кімнати {} ?'.format(key['data'].room),
                    user=self.user)
                self.choice.show()
                QtCore.QTimer.singleShot(10000, self.choice.close)
            else:
                taken_key = UserKeyLink.userkeylink_get_taken_key(key['data'].id)
                if taken_key['data']:
                    print 'This key already taken by user', taken_key['data'].user.firstname, ' ', taken_key['data'].user.lastname, 'at', taken_key['data'].date_taked.strftime('%d %b %Y, %H:%M')

    def exit(self):
        self.close()

    def open_settings_menu(self):
        self.adminForm.show()

