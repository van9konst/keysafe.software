from PyQt4 import QtGui

from Design import GetKeyWindow
from AdminForm.adminForm import AdminForm


class GetKeyWindow(QtGui.QMainWindow, GetKeyWindow.Ui_GetKeyWindow):
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
