from PyQt4 import QtGui

from design import new_user_design


class AddNewUser(QtGui.QMainWindow, new_user_design.Ui_AddUserWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.exit)

    def add_user_rfid_card(self):
        pass

    def exit(self):
        self.close()
