import sys  # We need sys so that we can pass argv to QApplication

from PyQt4 import QtGui  # Import the PyQt4 module we'll need

from AddNewUser.Design import AddNewUser
from AdminForm.Design import AdminForm
from GetKeyWindow.Design import GetKeyWindow
from MainWindow.Design import FirstWindow
from ReadCardWindow.Design import ReadCardWindow


# This file holds our MainWindow and all design related things

# it also keeps events etc that we defined in Qt Designer

class ReadCardWindow(QtGui.QMainWindow, ReadCardWindow.Ui_ReadKeyWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)


class MainFirstWindow(QtGui.QMainWindow, FirstWindow.Ui_FirstWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.btnBrowse.clicked.connect(self.get_key)

    def get_key(self):
        self.Get = NewWindow()
        self._new_window.show()


class AdminFormWindow(QtGui.QMainWindow, AdminForm.Ui_AdminFormMain):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)


class GetKeyWindow(QtGui.QMainWindow, GetKeyWindow.Ui_GetKeyWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)


class AddNewUserWindow(QtGui.QMainWindow, AddNewUser.Ui_AddUserWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)



def main():
    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    form = MainFirstWindow()  # We set the form to be our ExampleApp (design)
    form.showFullScreen()  # Show the form
    app.exec_()  # and execute the app


if __name__ == '__main__':
    main()