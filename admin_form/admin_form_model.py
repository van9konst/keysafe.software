from PyQt4 import QtGui

from design import admin_form_design
from new_user.new_user_model import AddNewUser
from new_room.new_room_model import AddNewRoom


class AdminForm(QtGui.QMainWindow, admin_form_design.Ui_AdminFormMain):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.new_user_window = AddNewUser()
        self.new_room_window = AddNewRoom()
        self.new_user.clicked.connect(self.add_user)
        self.new_key.clicked.connect(self.add_key)
        self.exit_to_main.clicked.connect(self.exit)

    def add_user(self):
        self.new_user_window.show()

    def add_key(self):
        self.new_room_window.show()

    def exit(self):
        self.close()
