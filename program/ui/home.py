from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

from program.utils import Utilities

class Home():
    def __init__(self, root, listener, uid):
        self.root = root
        self.initUI()
        self.uid = uid
        self.listener = listener

    def new_password(self):
        def _create():
            pass
        self.screen_lay.setRowStretch(1, 1)
        self.screen_lay.setRowStretch(99, 1)

        self.screen_lay.setColumnStretch(1, 3)
        self.screen_lay.setColumnStretch(3, 2)

        title_lbl = QLabel("Create new password")
        title_lbl.setFont(QFont('monospace', 24))
        title_lbl.setAlignment(Qt.AlignCenter)
        self.screen_lay.addWidget(title_lbl, 1, 1, 1, 3)

        login_lbl = QLabel("Login name:")
        login_lbl.setAlignment(Qt.AlignRight)
        self.screen_lay.addWidget(login_lbl, 2, 1)

        login_inp = QLineEdit()
        login_inp.setPlaceholderText("example@login.io")
        self.screen_lay.addWidget(login_inp, 2, 2)

        pass_lbl = QLabel("Password:")
        pass_lbl.setAlignment(Qt.AlignRight)
        self.screen_lay.addWidget(pass_lbl, 3, 1)

        pass_inp = QLineEdit()
        pass_inp.setEchoMode(QLineEdit.Password)
        pass_inp.setPlaceholderText("password123")
        self.screen_lay.addWidget(pass_inp, 3, 2)

        url_lbl = QLabel("URL/Application:")
        url_lbl.setAlignment(Qt.AlignRight)
        self.screen_lay.addWidget(url_lbl, 4, 1)

        url_inp = QLineEdit()
        url_inp.setPlaceholderText("www.facebook.com")
        self.screen_lay.addWidget(url_inp, 4, 2)

        desc_lbl = QLabel("Description:")
        desc_lbl.setAlignment(Qt.AlignRight)
        self.screen_lay.addWidget(desc_lbl, 5, 1)

        desc_inp = QLineEdit()
        desc_inp.setPlaceholderText("Social Media")
        self.screen_lay.addWidget(desc_inp, 5, 2)

        sep_lbl = QLabel(" ")
        self.screen_lay.addWidget(sep_lbl, 6, 1)

        create_btn = QPushButton("Create")
        create_btn.clicked.connect(_create)
        self.screen_lay.addWidget(create_btn, 7, 1, 1, 3)

    def upd_password(self):
        self.screen_lay.setRowStretch(99, 1)

    def find_password(self):
        self.screen_lay.setRowStretch(99, 1)

    def del_password(self):
        self.screen_lay.setRowStretch(99, 1)

    def initUI(self):
        def _new():
            Utilities.clear_layout(self.screen_lay)
            self.new_password()

        def _upd():
            Utilities.clear_layout(self.screen_lay)
            self.upd_password()

        def _find():
            Utilities.clear_layout(self.screen_lay)
            self.find_password()

        def _del():
            Utilities.clear_layout(self.screen_lay)
            self.del_password()

        def _off():
            Utilities.clear_layout(self.root)
            self.listener()

        main_layout = QVBoxLayout()
        self.root.addLayout(main_layout)

        # +---------+
        # | Buttons |
        # +---------+
        btn_lay = QHBoxLayout()
        main_layout.addLayout(btn_lay)

        new_btn = QPushButton("New Password")
        new_btn.clicked.connect(_new)
        btn_lay.addWidget(new_btn)

        upd_btn = QPushButton("Update Password")
        upd_btn.clicked.connect(_upd)
        btn_lay.addWidget(upd_btn)

        find_btn = QPushButton("Find Password")
        find_btn.clicked.connect(_find)
        btn_lay.addWidget(find_btn)

        del_btn = QPushButton("Delete Password")
        del_btn.clicked.connect(_del)
        btn_lay.addWidget(del_btn)

        sep_lbl = QLabel(" ")
        btn_lay.addWidget(sep_lbl)

        off_btn = QPushButton("Logout")
        off_btn.clicked.connect(_off)
        btn_lay.addWidget(off_btn)

        self.screen_lay = QGridLayout()
        self.screen_lay.setRowStretch(99, 1)
        main_layout.addLayout(self.screen_lay)
