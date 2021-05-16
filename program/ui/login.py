from PyQt5 import QtCore
from PyQt5.QtWidgets import *

from program.utils import Utilities

class Login():
    def __init__(self, root, listener):
        self.root = root
        self.initUI()
        self.listener = listener

    def press_login(self, user:str, password:str):
        self.listener(0)
    
    #0   1              2 
    #    +-------------+
    #1   | User:       |
    #2   | [         ] | 
    #3   | Password:   |
    #4   | [         ] |
    #5   | Password:   |
    #6   | [         ] |
    #7   |             |
    #8   |  {SUBMIT}   |
    #9   |   {BACK}    |
    #    +-------------+
    #10
    def press_register(self):
        def _submit():
            Utilities.clear_layout(self.root)
            self.initUI()
            
        def _back():
            Utilities.clear_layout(self.root)
            self.initUI()
            
        main_layout = QGridLayout()
        self.root.addLayout(main_layout)

        main_layout.setRowStretch(0, 1)
        main_layout.setRowStretch(10, 1)
        main_layout.setColumnStretch(0, 1)
        main_layout.setColumnStretch(2, 1)

        user_lbl = QLabel("User:")
        main_layout.addWidget(user_lbl, 1, 1)
        user_ent = QLineEdit()
        main_layout.addWidget(user_ent, 2, 1)

        password_lbl = QLabel("Password:")
        main_layout.addWidget(password_lbl, 3, 1)
        password_ent = QLineEdit()
        password_ent.setEchoMode(QLineEdit.Password)
        main_layout.addWidget(password_ent, 4, 1)

        password_lbl = QLabel("Confirm Password:")
        main_layout.addWidget(password_lbl, 5, 1)
        password_ent = QLineEdit()
        password_ent.setEchoMode(QLineEdit.Password)
        main_layout.addWidget(password_ent, 6, 1)

        break_lbl = QLabel("    ")
        main_layout.addWidget(break_lbl, 7, 1)
            
        submit_btn = QPushButton("Submit")
        submit_btn.clicked.connect(_submit)
        main_layout.addWidget(submit_btn, 8, 1)

        back_btn = QPushButton("Back")
        back_btn.clicked.connect(_back)
        main_layout.addWidget(back_btn, 9, 1)


    #0   1              2 
    #    +-------------+
    #1   | User:       |
    #2   | [         ] | 
    #3   | Password:   |
    #4   | [         ] |
    #5   |             |
    #6   |   {LOGIN}   |
    #7   |  {REGISTER} |
    #    +-------------+
    #8
    def initUI(self):

        def _login():
            self.press_login(user_ent.text(), password_ent.text())

        def _register():
            Utilities.clear_layout(self.root)
            self.press_register()

        main_layout = QGridLayout()
        self.root.addLayout(main_layout)

        main_layout.setRowStretch(0, 1)
        main_layout.setRowStretch(10, 1)
        main_layout.setColumnStretch(0, 1)
        main_layout.setColumnStretch(2, 1)

        user_lbl = QLabel("User:")
        main_layout.addWidget(user_lbl, 1, 1)
        user_ent = QLineEdit()
        main_layout.addWidget(user_ent, 2, 1)

        password_lbl = QLabel("Password:")
        main_layout.addWidget(password_lbl, 3, 1)
        password_ent = QLineEdit()
        password_ent.setEchoMode(QLineEdit.Password)
        main_layout.addWidget(password_ent, 4, 1)

        break_lbl = QLabel("    ")
        main_layout.addWidget(break_lbl, 5, 1)

        login_btn = QPushButton("Login")
        login_btn.clicked.connect(_login)
        main_layout.addWidget(login_btn, 6, 1)

        register_btn = QPushButton("Register")
        register_btn.clicked.connect(_register)
        main_layout.addWidget(register_btn, 7, 1)
