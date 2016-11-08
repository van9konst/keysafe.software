# -*- coding: utf-8 -*-
from PyQt4 import QtGui, QtCore
import zmq
from design import new_user_design
from info_window.info_model import InfoWindow
from database.models import User, Key


class AddNewUser(QtGui.QMainWindow, new_user_design.Ui_AddUserWindow):
    def __init__(self, first_user=None):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.first_user = first_user
        self.add_rfid_card.clicked.connect(self.connect_rfid_card)
        self.add_new_user.clicked.connect(self.create_user)
        self.exit_to_main.clicked.connect(self.exit)
        self.user = User
        self.key = Key
        self.firstname.clear()
        self.lastname.clear()
        self.rfid_card.clear()
        self.info_error = InfoWindow(label_text=u'Вибачте, сталася помилка, зверніться будь ласка до адміністратора')

    def connect_rfid_card(self):
        self.startReading()
        self.read_card = InfoWindow(label_text=u"Піднесіть карту", parent=self, hide_ok=True, read='user')
        self.read_card.show()
        QtCore.QTimer.singleShot(5000, self.read_card.return_rfid)

    def startReading(self):
        context = zmq.Context()
        socket = context.socket(zmq.REQ)
        socket.connect('tcp://127.0.0.1:5555')
        socket.send("readTeacherId")

    def create_user(self):
        firstname = unicode(self.firstname.text().toUtf8(), encoding="UTF-8")
        lastname = unicode(self.lastname.text().toUtf8(), encoding="UTF-8")
        rfid = unicode(self.rfid_card.text().toUtf8(), encoding="UTF-8")
        admin = self.admin_checkbox.isChecked()
        try:
            if self.user.get_by_rfid(rfid)['warnings'] and self.key.get_by_rfid(rfid)['warnings']:
                if self.first_user:
                    admin = True
                new_user = self.user.create(firstname, lastname, rfid, admin)
                if new_user['errors'] or new_user['warnings']:
                    self.info_error.show()
                    QtCore.QTimer.singleShot(5000, self.info_error.close)
                else:
                    self.info = InfoWindow(label_text=u'Користувача додано!', parent=self)
                    self.info.show()
                    QtCore.QTimer.singleShot(5000, self.info.close)
                    QtCore.QTimer.singleShot(5000, self.close)
            else:
                self.info = InfoWindow(label_text=u'Такий RFID ключ вже зареєстрований у системі')
                self.info.show()
                QtCore.QTimer.singleShot(5000, self.info.close)
        except:
            self.info_error.show()
            QtCore.QTimer.singleShot(5000, self.info_error.close)

    def exit(self):
        self.firstname.clear()
        self.lastname.clear()
        self.rfid_card.clear()
        self.close()
