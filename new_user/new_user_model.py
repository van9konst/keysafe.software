from PyQt4 import QtGui

from Design import AddNewUser


class AddNewUser(QtGui.QMainWindow, AddNewUser.Ui_AddUserWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.exit)

    def exit(self):
        self.close()
