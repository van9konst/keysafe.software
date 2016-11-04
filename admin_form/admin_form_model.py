from PyQt4 import QtGui

from design import admin_form_design
from new_user.new_user_model import AddNewUser
from new_room.new_room_model import AddNewRoom
from delete_users.delete_users_model import DeleteUsersWindow


class AdminForm(QtGui.QMainWindow, admin_form_design.Ui_AdminFormMain):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.new_user_window = AddNewUser()
        self.new_room_window = AddNewRoom()
        self.delete_users_window = DeleteUsersWindow()
        self.new_user.clicked.connect(self.add_user)
        self.new_key.clicked.connect(self.add_key)
        self.remove_user.clicked.connect(self.delete_users)
        self.remove_key.clicked.connect(self.delete_keys)
        self.exit_to_main.clicked.connect(self.exit)

    def add_user(self):
        self.new_user_window.show()

    def add_key(self):
        self.new_room_window.show()

    def delete_users(self):
        self.delete_users_window.show()

    def delete_keys(self):
        pass

    def exit(self):
        self.close()
