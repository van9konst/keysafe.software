from PyQt4 import QtGui

import os
import sys

keysafe_dir = os.path.expanduser("~/keysafe.software")
sys.path.append(keysafe_dir)
from design import chooice

class ChooiceWindow(QtGui.QMainWindow, chooice.Ui_ChooiceWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.no.clicked.connect(self.exit)

    def exit(self):
        self.close()

    def open_chooice(self):
        self.get_keys_window.show()
