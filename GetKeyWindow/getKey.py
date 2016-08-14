from PyQt4 import QtGui

from Design import GetKeyWindow


class GetKeyWindow(QtGui.QMainWindow, GetKeyWindow.Ui_GetKeyWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.exit_to_main.clicked.connect(self.exit)

    def exit(self):
        self.close()