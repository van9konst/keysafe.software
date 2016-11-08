# -*- coding: utf-8 -*-
import zmq
from PyQt4 import QtGui, QtCore

from design import info
from database.models import UserKeyLink


class InfoWindow(QtGui.QMainWindow, info.Ui_InfoWindow):
    def __init__(self, label_text=None, parent=None, previous_parent=None, hide_ok=None, read=None):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.read = read
        self.parent = parent
        self.previous_parent = previous_parent
        if hide_ok:
            self.button_ok.setVisible(False)
        self.label.setText(u'<html><head/><body><p align="center"><span style="font-size:26pt;font-weight:600;">{}</span></p> </body></html>'.format(label_text))
        self.button_ok.clicked.connect(self.ok)

    def ok(self):
        if self.previous_parent:
            self.previous_parent.close()
        elif self.parent:
            self.parent.close()
        self.close()

    def return_key(self):
        context = zmq.Context()
        socket = context.socket(zmq.REQ)
        socket.connect('tcp://127.0.0.1:5555')
        socket.send("getTeacherId")
        msg = socket.recv()
        if msg != '0':
            returning = UserKeyLink.returning_key(msg)
            if returning['warnings']:
                self.info = InfoWindow(label_text=u"Цей ключ вже повернуто!", parent=self)
                self.info.show()
                QtCore.QTimer.singleShot(3000, self.info.close)
                QtCore.QTimer.singleShot(3000, self.close)
            elif returning['errors']:
                self.info = InfoWindow(label_text=u"Сталася помилка,зверністья до адміністратора!", parent=self)
                self.info.show()
                QtCore.QTimer.singleShot(3000, self.info.close)
                QtCore.QTimer.singleShot(3000, self.close)
            else:
                self.info = InfoWindow(label_text=u"Вставте ключ у приймач", parent=self)
                self.info.show()
                QtCore.QTimer.singleShot(5000, self.info.close)
                QtCore.QTimer.singleShot(5000, self.close)
        else:
            self.info = InfoWindow(label_text=u"Ключа не виявлено", parent=self)
            self.info.show()
            QtCore.QTimer.singleShot(2000, self.info.close)
            QtCore.QTimer.singleShot(2000, self.close)

    def return_rfid(self):
        context = zmq.Context()
        socket = context.socket(zmq.REQ)
        socket.connect('tcp://127.0.0.1:5555')
        socket.send("getTeacherId")
        msg = socket.recv()
        if msg != '0':
            if self.read is "user":
                self.parent.rfid_card.clear()
                self.parent.rfid_card.setText(msg)
            elif self.read is "key":
                self.parent.rfid_chip.clear()
                self.parent.rfid_chip.setText(msg)
            self.info = InfoWindow(label_text=u"Ідентифікатор додано", parent=self)
            self.info.show()
            QtCore.QTimer.singleShot(2000, self.info.close)
            QtCore.QTimer.singleShot(2000, self.close)
        else:
            self.info = InfoWindow(label_text=u"Ідентифікатора не знайдено", parent=self)
            self.info.show()
            QtCore.QTimer.singleShot(2000, self.info.close)
            QtCore.QTimer.singleShot(2000, self.close)

