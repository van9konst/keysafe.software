from PyQt4 import QtGui

from design import read_card_design


class ReadCardWindow(QtGui.QMainWindow, read_card_design.Ui_ReadKeyWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)