from PyQt4 import QtGui

from design import get_key_design
from admin_form.admin_form_model import AdminForm


class GetKeyWindow(QtGui.QMainWindow, get_key_design.Ui_GetKeyWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.exit_to_main.clicked.connect(self.exit)
        self.adminForm = AdminForm()
        self.admin_settings_button.clicked.connect(self.open_settings_menu)

    def exit(self):
        self.close()

    def open_settings_menu(self):
        self.adminForm.showFullScreen()
