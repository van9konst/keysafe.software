# -*- coding: utf-8 -*-
import sys
import os
import zmq
from PyQt4 import QtGui, QtCore

keysafe_dir = os.path.expanduser("~/keysafe.software")
sys.path.append(keysafe_dir)

from main.design import main_design
from read_card.read_card_model import ReadCardWindow
from database.models import User
from info_window.info_model import InfoWindow
from new_user.new_user_model import AddNewUser


class MainFirstWindow(QtGui.QMainWindow, main_design.Ui_FirstWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.get_key.clicked.connect(self.get_the_keys)
        self.return_key.clicked.connect(self.put_the_keys)
        self.info_error = InfoWindow(label_text=u'Вибачте, сталася помилка, зверніться будь ласка до адміністратора')

    def authenticate_user(self):
        self.startReading()
        self.read_card_window = ReadCardWindow()
        self.read_card_window.show()
        QtCore.QTimer.singleShot(4000, self.read_card_window.read_card_result)

    def get_the_keys(self):
        if User.get_all()['warnings']:
            self.info = InfoWindow(label_text=u"Перший запуск програми, будь ласка створіть користувача!")
            self.info.show()
            self.new_user = AddNewUser()
            QtCore.QTimer.singleShot(3000, self.info.close)
            QtCore.QTimer.singleShot(3000, self.new_user.show)
        else:
            self.authenticate_user()

    def put_the_keys(self):
        self.startReading()
        self.read_card = InfoWindow(label_text=u"Піднесіть ключ до зчитувача", hide_ok=True)
        self.read_card.show()
        QtCore.QTimer.singleShot(5000, self.read_card.return_key)

    def startReading(self):
        context = zmq.Context()
        socket = context.socket(zmq.REQ)
        socket.connect('tcp://127.0.0.1:5555')
        socket.send("readTeacherId")


def main():
    app = QtGui.QApplication(sys.argv)
    form = MainFirstWindow()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()
