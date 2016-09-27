import sys
import os
import time
import gevent
from gevent import Greenlet
from PyQt4 import QtGui, QtCore

keysafe_dir = os.path.expanduser("~/keysafe.software")
sys.path.append(keysafe_dir)
from main.design import main_design
from get_key.get_key_model import GetKeyWindow
from read_card.read_card_model import ReadCardWindow
from welcome_window.welcome_model import WelcomeWindow
from database.models import User, Key, UserKeyLink


class MainFirstWindow(QtGui.QMainWindow, main_design.Ui_FirstWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.get_keys_window = GetKeyWindow()
        self.welcome = WelcomeWindow()
        self.get_key.clicked.connect(self.get_the_keys)

    def authenticate_user(self):
        # TODO: open scanning window for 30 sec
        # TODO: run scanning script
        # TODO: close after 30 second \ return bad answer \ get rights
        return

    def open_welcome_window(self, label_text):
        self.welcome = WelcomeWindow(label_text)
        self.welcome.show()
        QtCore.QTimer.singleShot(1000, self.welcome.close)

    def get_key_window(self):
        QtCore.QTimer.singleShot(1000, self.get_keys_window.show)

    def get_the_keys(self):
        # TODO: Open window with user auth
        self.open_welcome_window("Volodymyr Vozniak")
        self.get_key_window()

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
