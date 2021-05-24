from PyQt5 import QtCore
from PyQt5.QtWidgets import *

from program.ui import *
from program.utils import Utilities
from program.filemg import FileMG

class PyQtGUI(QWidget):
    def __init__(self,):
        super().__init__()
        self.initUI()

    def closeEvent(self, event):
        try:
            FileMG.encrypt_file()
        except Exception as err:
            print(err)
        finally:
            event.accept()

    def after_login(self, user_id):
        Utilities.clear_layout(self.layout)
        Home(self.layout, self.login, user_id)


    def login(self):
        FileMG.logout()
        Login(self.layout, self.after_login, False)

    def initUI(self):
        self.layout = QVBoxLayout()
        Login(self.layout, self.after_login, FileMG.any_user())

        self.setLayout(self.layout)
        self.setWindowTitle("PD4 Password Manager")
        self.setGeometry(300, 300, 600, 400)
        self.show()
