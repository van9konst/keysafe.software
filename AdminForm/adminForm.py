from PyQt4 import QtGui

from Design import AdminForm


class AdminForm(QtGui.QMainWindow, AdminForm.Ui_AdminFormMain):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)