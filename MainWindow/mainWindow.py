import sys

from PyQt4 import QtGui

from MainWindow.Design import FirstWindow
from GetKeyWindow.getKey import GetKeyWindow


class MainFirstWindow(QtGui.QMainWindow, FirstWindow.Ui_FirstWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.keys_window = GetKeyWindow()
        self.get_key.clicked.connect(self.get_the_keys)

    def get_the_keys(self):
        # TODO: Open window with user auth
        self.keys_window.showFullScreen()

    def put_the_keys(self):
        # TODO: Add a window for put keys
        return


def main():
    app = QtGui.QApplication(sys.argv)
    form = MainFirstWindow()
    form.showFullScreen()
    app.exec_()


if __name__ == '__main__':
    main()