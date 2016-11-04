# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore

from design import delete_users_design
from choice_window.choice_model import ChoiceWindow
from info_window.info_model import InfoWindow
from database.models import Key, UserKeyLink, User



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


class DeleteUsersWindow(QtGui.QMainWindow, delete_users_design.Ui_DeleteUsers):
    def __init__(self, users):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.exit_to_main.clicked.connect(self.exit)
        if users:
            buttons = {}
            row_count = 0
            for user in users:
                buttons[user.id] = QtGui.QPushButton(self.scrollAreaWidgetContents)
                buttons[user.id].setFixedSize(150, 100)
                buttons[user.id].setStyleSheet('QPushButton {;''color: black;'
                                               'font: 55 30pt DejaVu Sans Mono for Powerline;}')
                buttons[user.id].setText(_translate("DeleteUsers", str(user.firstname.encode('utf-8')) + ' \n ' + str(user.lastname.encode('utf-8')), None))
                buttons[user.id].setObjectName(user.rfid_card)
                buttons[user.id].clicked.connect(self.button_clicked)
                self.gridLayout_2.addWidget(buttons[user.id], int(row_count % 3), int(row_count / 3))
                row_count += 1

    def button_clicked(self):
        sender = self.sender()
        user = User.get_by_rfid(str(sender.objectName()))
        if user['data']:
            self.choice = ChoiceWindow(
                operation='delete_user',
                label_text=u'Видалити користувача {} ?'.format(user['data'].firstname + ' ' + user['data'].lastname),
                user=user['data'].rfid_card)
            self.choice.show()
            QtCore.QTimer.singleShot(10000, self.choice.close)
        else:
            self.info = InfoWindow(
                label_text=u'Вибачте, сталася помилка,зверніться будь ласка до адміністратора'
            )
            self.info.show()
            QtCore.QTimer.singleShot(5000, self.info.close)

    def exit(self):
        self.close()

