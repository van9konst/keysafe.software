# -*- coding: utf8 -*-
from PyQt4 import QtGui, QtCore

import zmq
from design import read_card_design
from info_window.info_model import InfoWindow
from welcome_window.welcome_model import WelcomeWindow
from get_key.get_key_model import GetKeyWindow
from database.models import User, Key


class ReadCardWindow(QtGui.QMainWindow, read_card_design.Ui_ReadKeyWindow):
    def __init__(self, parent=None):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.parent = parent
        self.info_error = InfoWindow(label_text=u'Вибачте, сталася помилка, зверніться будь ласка до адміністратора')

    def read_card_result(self):
        context = zmq.Context()
        socket = context.socket(zmq.REQ)
        socket.connect('tcp://127.0.0.1:5555')
        socket.send("getTeacherId")
        msg = socket.recv()
        if msg != '0':
            check_user = User.get_by_rfid(msg)
            if check_user['warnings']:
                self.close()
            else:
                self.login(check_user['data'])
                self.close()
        else:
            self.close()

    def welcome_window(self, label_text):
        self.welcome = WelcomeWindow(label_text)
        self.welcome.show()
        QtCore.QTimer.singleShot(5000, self.welcome.close)

    def get_key_window(self, keys, user):
        self.get_keys_window = GetKeyWindow(keys, user)
        QtCore.QTimer.singleShot(5000, self.get_keys_window.show)

    def login(self, user):
        username = user.firstname + u' ' + user.lastname
        self.welcome_window(username)
        keys = Key.get_all()
        if keys['errors']:
            self.info_error.show()
            QtCore.QTimer.singleShot(5000, self.info_error.close)
        elif keys['warnings']:
            self.get_key_window(keys=None, user=None)
        else:
            self.get_key_window(keys['data'], user=user)
