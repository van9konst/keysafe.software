from PyQt4 import QtGui

from Design import AdminForm
from AddNewUser.addNewUser import AddNewUser


class AdminForm(QtGui.QMainWindow, AdminForm.Ui_AdminFormMain):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.addNewUser = AddNewUser()

        self.add_new_card.clicked.connect(self.register_user)
        self.exit_to_main.clicked.connect(self.exit)

    def register_user(self):
        self.addNewUser.showFullScreen()

    def exit(self):
        self.close()
