# -*- coding: utf-8 -*-
from PyQt4 import QtGui, QtCore

from design import new_user_design
from info_window.info_model import InfoWindow
from database.models import User, Key


class AddNewUser(QtGui.QMainWindow, new_user_design.Ui_AddUserWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.add_rfid_card.clicked.connect(self.connect_rfid_card)
        self.add_new_user.clicked.connect(self.create_user)
        self.exit_to_main.clicked.connect(self.exit)
        self.user = User
        self.key = Key

    def connect_rfid_card(self):
        pass

    def create_user(self):
        firstname = unicode(self.firstname.text().toUtf8(), encoding="UTF-8")
        lastname = unicode(self.lastname.text().toUtf8(), encoding="UTF-8")
        rfid = unicode(self.rfid_card.text().toUtf8(), encoding="UTF-8")
        admin = self.admin_checkbox.isChecked()
        try:
            if self.user.get_by_rfid(rfid)['warnings'] and self.key.get_by_rfid(rfid)['warnings']:
                self.user.create(firstname, lastname, rfid, admin)
                self.info = InfoWindow(label_text=u'Користувача додано!')
                self.info.show()
                QtCore.QTimer.singleShot(5000, self.info.close)
            else:
                self.info = InfoWindow(label_text=u'Такий RFID ключ вже зареєстрований у системі')
                self.info.show()
                QtCore.QTimer.singleShot(5000, self.info.close)
        except:
            self.info = InfoWindow(label_text=u'Вибачте, сталася помилка, зверніться будь ласка до адміністратора')
            self.info.show()
            QtCore.QTimer.singleShot(5000, self.info.close)

    def exit(self):
        self.close()
