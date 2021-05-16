from PyQt5 import QtCore
from PyQt5.QtWidgets import *

from program.ui import *
from program.utils import Utilities

class PyQtGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()


    def after_login(self, user_id):
        Utilities.clear_layout(self.layout)
        Home(self.layout, self.login, user_id)


    def login(self):
        Login(self.layout, self.after_login)

    def initUI(self):
        self.layout = QVBoxLayout()
        Login(self.layout, self.after_login)

        self.setLayout(self.layout)
        self.setWindowTitle("PD4 Password Manager")
        self.setGeometry(300, 300, 600, 400)
        self.show()
