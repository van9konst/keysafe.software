# -*- coding: utf-8 -*-

from PyQt4 import QtGui

from design import info


class InfoWindow(QtGui.QMainWindow, info.Ui_InfoWindow):
    def __init__(self, label_text=None, parent=None):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.parent = parent
        self.label.setText(u'<html><head/><body><p align="center"><span style="font-size:26pt;font-weight:600;">{}</span></p> </body></html>'.format(label_text))
        self.button_ok.clicked.connect(self.ok)

    def ok(self):
        if self.parent:
            self.parent.close()
        self.close()
