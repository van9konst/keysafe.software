# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore

from design import choice
from database.models import UserKeyLink, User, Key
from info_window.info_model import InfoWindow
from hardware.magnet_driver import Magnet
from hardware.motor_driver_a4988 import MotorDRV_a4988
from hardware.constants import *


class ChoiceWindow(QtGui.QMainWindow, choice.Ui_ChoiceWindow):
    def __init__(self, label_text=None, user=None, key=None, operation=None, parent=None):
        super(self.__class__, self).__init__()
        self.mtr1 = MotorDRV_a4988(motor1_step, motor1_dir, motors_enable)
        self.mtr2 = MotorDRV_a4988(motor2_step, motor2_dir, motors_enable)
        self.mgn = Magnet(magnet)
        self.parent = parent
        self.setupUi(self)
        self.user = user
        self.key = key
        self.operation = operation
        self.label.setText(u'<html><head/><body><p align="center"><span style="font-size:21pt;font-weight:600;"> {} </span></p></body></html>'.format(label_text))
        if self.operation is 'get_key':
            self.yes.clicked.connect(self.press_yes_get_key)
        elif self.operation is 'delete_user':
            self.yes.clicked.connect(self.press_yes_delete_user)
        elif self.operation is 'delete_key':
            self.yes.clicked.connect(self.press_yes_delete_key)
        self.no.clicked.connect(self.press_no)

    def press_no(self):
        if self.operation != 'get_key':
            self.parent.close()
        self.close()

    def press_yes_get_key(self):
        try:
            pppath = "50011 50012"
            for comnd in pppath.split():
                motor = int(comnd[-1])
                direction = int(comnd[-2])
                steps = int(comnd[:-2])
                if motor is 1:
                    self.mtr1.spin(steps, direction)  # 500 1 1
                if motor is 2:
                    self.mtr2.spin(steps, direction)
            for comnd in pppath.split()[::-1]:
                    motor = int(comnd[-1])
                    direction = 0 if int(comnd[-2]) == 1 else 1
                    steps = int(comnd[:-2])
                    if motor is 1:
                        self.mtr1.spin(steps, direction)  # 500 1 1
                    if motor is 2:
                        self.mtr2.spin(steps, direction)

            #self.mgn.up()
            # self.mtr1.spin(500, 1)  # 500 1 1
            # self.mtr2.spin(500, 1)  # 500 1 2
            # self.mtr2.spin(500, 0)  # 500 1 1
            # self.mtr1.spin(500, 0)  # 500 1 2
           # self.mgn.down()
            UserKeyLink.getting_key(self.user, self.key)['data']
            # TODO: run motors and magnet
        except Exception as e:
            print e
        self.parent.close()
        self.close()
        # TODO: show waiting window

    def press_yes_delete_user(self):
        user = User.get_by_rfid(self.user)['data']
        deleted = User.delete(user)
        if deleted['data'] is True:
            self.info = InfoWindow(label_text=u'Користувача видалено', parent=self, previous_parent=self.parent)
            self.info.show()
            QtCore.QTimer.singleShot(5000, self.info.close)
            QtCore.QTimer.singleShot(5000, self.close)
            QtCore.QTimer.singleShot(5000, self.parent.close)
        else:
            self.info = InfoWindow(label_text=u'Вибачте, сталася помилка,зверніться будь ласка до адміністратора')
            self.info.show()
            QtCore.QTimer.singleShot(5000, self.info.close)
            QtCore.QTimer.singleShot(5000, self.close)
            QtCore.QTimer.singleShot(5000, self.parent.close)

    def press_yes_delete_key(self):
        key = Key.get_by_rfid(self.key)['data']
        status = key.status
        deleted = User.delete(key)
        if deleted['data'] is True:
            self.info = InfoWindow(label_text=u'Ключ видалено', parent=self, previous_parent=self.parent)
            self.info.show()
            if status is True:
                return True
                # TODO: start returning keys in keys in box
            QtCore.QTimer.singleShot(5000, self.info.close)
            QtCore.QTimer.singleShot(5000, self.close)
            QtCore.QTimer.singleShot(5000, self.parent.close)
        else:
            self.info = InfoWindow(label_text=u'Вибачте, сталася помилка,зверніться будь ласка до адміністратора')
            self.info.show()
            QtCore.QTimer.singleShot(5000, self.info.close)
            QtCore.QTimer.singleShot(5000, self.close)
            QtCore.QTimer.singleShot(5000, self.parent.close)


