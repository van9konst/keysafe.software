from PyQt4 import QtGui

from Design import ReadCardWindow


class ReadCardWindow(QtGui.QMainWindow, ReadCardWindow.Ui_ReadKeyWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)