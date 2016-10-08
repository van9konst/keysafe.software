# -*- coding: utf-8 -*-

from PyQt4 import QtGui

from design import welcome


class WelcomeWindow(QtGui.QMainWindow, welcome.Ui_WelcomeWindow):
    def __init__(self, label_text=None):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.label.setText(u'<html><head/><body><p align="center"><span style="font-size:26pt;font-weight:600;">{}</span></p> </body></html>'.format(label_text))

    def close_welcome_window(self):
        self.close()
