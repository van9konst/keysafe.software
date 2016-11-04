# -*- coding: utf-8 -*-
import sys
import os
from PyQt4 import QtGui, QtCore

keysafe_dir = os.path.expanduser("~/keysafe.software")
sys.path.append(keysafe_dir)

from main.design import main_design
from get_key.get_key_model import GetKeyWindow
from read_card.read_card_model import ReadCardWindow
from welcome_window.welcome_model import WelcomeWindow
from database.models import User, Key
from info_window.info_model import InfoWindow
from new_user.new_user_model import AddNewUser


class MainFirstWindow(QtGui.QMainWindow, main_design.Ui_FirstWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.get_key.clicked.connect(self.get_the_keys)
        self.info_error = InfoWindow(label_text=u'Вибачте, сталася помилка, зверніться будь ласка до адміністратора')

    def authenticate_user(self):
        self.read_card_window = ReadCardWindow()
        self.read_card_window.show()
        QtCore.QTimer.singleShot(10000, self.read_card_window.close)

        # TODO: open scanning window for 30 sec
        # TODO: run scanning script
        # TODO: close after 30 second \ return bad answer \ get rights

    def welcome_window(self, label_text):
        self.welcome = WelcomeWindow(label_text)
        self.welcome.show()
        QtCore.QTimer.singleShot(2000, self.welcome.close)

    def get_key_window(self, keys, user):
        self.get_keys_window = GetKeyWindow(keys, user)
        QtCore.QTimer.singleShot(2000, self.get_keys_window.show) # time when welcome window close and this window open

        # Time to close get_key_window
        #QtCore.QTimer.singleShot(60000, self.get_keys_window.close)

    def get_the_keys(self):
        if User.get_all()['warnings']:
            self.info = InfoWindow(label_text=u"Перший запуск програми, будь ласка створіть користувача!")
            self.info.show()
            self.new_user = AddNewUser()
            QtCore.QTimer.singleShot(3000, self.info.close)
            QtCore.QTimer.singleShot(3000, self.new_user.show)
        else:
            # TODO: Open window with user auth
            user = User.get_by_rfid("12334")['data']
            #user = u'Vova'
            #self.authenticate_user()
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
                # TODO: Need return error window
        # else:
        #     print 'Bad day motherfucker'
        #     return False

    def put_the_keys(self):
        # TODO: Add a window for put keys
        return


def main():
    app = QtGui.QApplication(sys.argv)
    form = MainFirstWindow()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()
