# -*- coding: utf-8 -*-

from PyQt4 import QtGui

from design import chooice

class ChooiceWindow(QtGui.QMainWindow, chooice.Ui_ChooiceWindow):
    def __init__(self, label_text=None):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.label_text= "text"
        self.label.setText('<html><head/><body><p align="center"><span style="font-size:24pt;font-weight:600;">{}</span></p> </body></html>'.format(label_text))
        self.yes.clicked.connect(self.press_yes)
        self.no.clicked.connect(self.press_no)

    def press_no(self):
        self.close()

    def press_yes(self):
        self.close()
