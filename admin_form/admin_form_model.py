# -*- coding: utf-8 -*-
from PyQt4 import QtGui, QtCore

from design import admin_form_design
from new_user.new_user_model import AddNewUser
from new_room.new_room_model import AddNewRoom
from delete_users.delete_users_model import DeleteUsersWindow
from delete_keys.delete_keys_model import DeleteKeysWindow
from info_window.info_model import InfoWindow
from database.models import User, Key


class AdminForm(QtGui.QMainWindow, admin_form_design.Ui_AdminFormMain):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.new_user_window = AddNewUser()
        self.new_room_window = AddNewRoom()
        self.new_user.clicked.connect(self.add_user)
        self.new_key.clicked.connect(self.add_key)
        self.remove_user.clicked.connect(self.delete_users)
        self.remove_key.clicked.connect(self.delete_keys)
        self.exit_to_main.clicked.connect(self.exit)
        self.info_error = InfoWindow(label_text=u'Вибачте, сталася помилка, зверніться будь ласка до адміністратора')

    def add_user(self):
        self.new_user_window.show()

    def add_key(self):
        self.new_room_window.show()

    def delete_users(self):
        users = User.get_all()
        if users['data']:
            self.delete_users_window = DeleteUsersWindow(users['data'])
            self.delete_users_window.show()
        elif users['warnings']:
            self.info = InfoWindow(label_text=u"Немає користувачів яких можна видалити")
            self.info.show()
            QtCore.QTimer.singleShot(5000, self.info.close)
        else:
            self.info_error.show()
            QtCore.QTimer.singleShot(5000, self.info_error.close)

    def delete_keys(self):
        keys = Key.get_all()
        if keys['data']:
            self.delete_keys_window = DeleteKeysWindow(keys['data'])
            self.delete_keys_window.show()
        elif keys['warnings']:
            self.info = InfoWindow(label_text=u"Немає ключів які можна видалити")
            self.info.show()
            QtCore.QTimer.singleShot(5000, self.info.close)
        else:
            self.info_error.show()
            QtCore.QTimer.singleShot(5000, self.info_error.close)

    def exit(self):
        self.close()
