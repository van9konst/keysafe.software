import sys  # We need sys so that we can pass argv to QApplication

from PyQt4 import QtGui  # Import the PyQt4 module we'll need

from MainWindow.Design import FirstWindow
from GetKeyWindow.getKey import GetKeyWindow


class MainFirstWindow(QtGui.QMainWindow, FirstWindow.Ui_FirstWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.get_key.clicked.connect(self.authorize)

    def authorize(self):
        self.keys_window = GetKeyWindow()
        self.keys_window.showFullScreen()


def main():
    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    form = MainFirstWindow()  # We set the form to be our ExampleApp (design)
    form.showFullScreen()  # Show the form
    app.exec_()  # and execute the app


if __name__ == '__main__':
    main()