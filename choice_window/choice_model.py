# -*- coding: utf-8 -*-

from PyQt4 import QtGui

from design import choice
from database.models import UserKeyLink


class ChoiceWindow(QtGui.QMainWindow, choice.Ui_ChoiceWindow):
    def __init__(self, label_text=None, user=None, key=None, operation=None):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.user = user
        self.key = key
        self.label.setText(u'<html><head/><body><p align="center"><span style="font-size:26pt;font-weight:600;">{}</span></p> </body></html>'.format(label_text))
        if operation is 'get_key':
            self.yes.clicked.connect(self.press_yes_get_key)
        self.no.clicked.connect(self.press_no)

    def press_no(self):
        self.close()

    def press_yes_get_key(self):
        try:
            UserKeyLink.userkeylink_get_key(self.user, self.key)['data']
        except Exception as e:
            print e
        self.close()



