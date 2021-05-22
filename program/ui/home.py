from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.Qt import QRect

from program.utils import Utilities

class Popup(QWidget):
    def __init__(self, btn_name:str, btn_func):
        QWidget.__init__(self)
        self.btn_name = btn_name
        self.btn_func = btn_func
        self.setWindowTitle(self.btn_name + " password")

        self.initUI()
    
    def initUI(self):
        layout = QGridLayout()
        self.setLayout(layout)

        layout.setRowStretch(1, 1)
        layout.setRowStretch(99, 1)

        layout.setColumnStretch(1, 3)
        layout.setColumnStretch(3, 2)

        login_lbl = QLabel("Login name:")
        login_lbl.setAlignment(Qt.AlignRight)
        layout.addWidget(login_lbl, 2, 1)

        login_inp = QLineEdit()
        login_inp.setPlaceholderText("example@login.io")
        layout.addWidget(login_inp, 2, 2)

        pass_lbl = QLabel("Password:")
        pass_lbl.setAlignment(Qt.AlignRight)
        layout.addWidget(pass_lbl, 3, 1)

        pass_inp = QLineEdit()
        pass_inp.setEchoMode(QLineEdit.Password)
        pass_inp.setPlaceholderText("password123")
        layout.addWidget(pass_inp, 3, 2)

        url_lbl = QLabel("URL/Application:")
        url_lbl.setAlignment(Qt.AlignRight)
        layout.addWidget(url_lbl, 4, 1)

        url_inp = QLineEdit()
        url_inp.setPlaceholderText("www.facebook.com")
        layout.addWidget(url_inp, 4, 2)

        desc_lbl = QLabel("Description:")
        desc_lbl.setAlignment(Qt.AlignRight)
        layout.addWidget(desc_lbl, 5, 1)

        desc_inp = QLineEdit()
        desc_inp.setPlaceholderText("Social Media")
        layout.addWidget(desc_inp, 5, 2)

        sep_lbl = QLabel(" ")
        layout.addWidget(sep_lbl, 6, 1)

        create_btn = QPushButton(self.btn_name)
        create_btn.clicked.connect(self.btn_func)
        layout.addWidget(create_btn, 7, 1, 1, 3)

class Home():
    def __init__(self, root, listener, uid):
        self.root = root
        self.initUI()
        self.uid = uid
        self.listener = listener

    def new_password(self):
        def _create():
            pass

        self.popup = Popup("Create", _create)
        self.popup.show()

    def upd_password(self):
        def _update():
            pass
        self.popup = Popup("Update", _update)
        self.popup.show()

    def find_password(self):
        def _search():
            pass

        def _next():
            self.entry_id += 1
            if len(self.entry_arr) < self.entry_id - 1:
                self.entry_id = len(self.entry_arr) - 1
            _draw_list()

        def _prev():
            self.entry_id -= 1
            if self.entry_id < 0:
                self.entry_id = 0
            _draw_list()

        def _draw_list():
            Utilities.clear_layout(entry_layout)

            login_lbl = QLabel("Login name:")
            login_lbl.setAlignment(Qt.AlignCenter)
            entry_layout.addWidget(login_lbl, 0, 0)

            pass_lbl = QLabel("Password:")
            pass_lbl.setAlignment(Qt.AlignCenter)
            entry_layout.addWidget(pass_lbl, 0, 1)

            url_lbl = QLabel("URL/Application:")
            url_lbl.setAlignment(Qt.AlignCenter)
            entry_layout.addWidget(url_lbl, 0, 4)

            desc_lbl = QLabel("Description:")
            desc_lbl.setAlignment(Qt.AlignCenter)
            entry_layout.addWidget(desc_lbl, 0, 5)

            for i in range(0, 10):
                if i + self.entry_id >= len(self.entry_arr):
                    break;
                login_inp = QLineEdit()
                login_inp.setReadOnly(True)
                login_inp.setPlaceholderText("example@login.io")
                entry_layout.addWidget(login_inp, i, 0)

                pass_inp = QLineEdit()
                pass_inp.setReadOnly(True)
                pass_inp.setPlaceholderText("password123")
                entry_layout.addWidget(pass_inp, i, 1)

                show_btn = QPushButton("*")
                show_btn.clicked.connect(_search)
                entry_layout.addWidget(show_btn, i, 2)

                copy_btn = QPushButton("Copy")
                copy_btn.clicked.connect(_search)
                entry_layout.addWidget(copy_btn, i, 3)

                url_inp = QLineEdit()
                url_inp.setReadOnly(True)
                url_inp.setPlaceholderText("www.facebook.com")
                entry_layout.addWidget(url_inp, i, 4)

                desc_inp = QLineEdit()
                desc_inp.setReadOnly(True)
                desc_inp.setPlaceholderText("Social Media")
                entry_layout.addWidget(desc_inp, i, 5)

        self.entry_id = 0
        self.entry_arr = []

        layout = QGridLayout()
        self.screen_lay.addLayout(layout)

        layout.setRowStretch(1, 1)
        layout.setRowStretch(99, 1)

        layout.setColumnStretch(2, 1)


        sep_lbl = QLabel(" ")
        layout.addWidget(sep_lbl, 1, 1)

        login_lbl = QLabel("Login name:")
        login_lbl.setAlignment(Qt.AlignRight)
        layout.addWidget(login_lbl, 2, 1)

        login_inp = QLineEdit()
        login_inp.setPlaceholderText("example@login.io")
        layout.addWidget(login_inp, 2, 2,)

        create_btn = QPushButton("Search")
        create_btn.clicked.connect(_search)
        layout.addWidget(create_btn, 2, 3,)

        sep_lbl = QLabel(" ")
        layout.addWidget(sep_lbl, 3, 1)


        entry_layout = QGridLayout()
        entry_layout.setColumnStretch(5, 1)

        entry_group = QGroupBox("Password list:")
        entry_group.setLayout(entry_layout)
        layout.addWidget(entry_group, 4, 1, 1, 4)

        _draw_list()

        page_btn_lay = QHBoxLayout()
        layout.addLayout(page_btn_lay, 5, 1, 1, 3)

        page_btn_lay.addStretch()

        prev_btn = QPushButton("Prev")
        prev_btn.clicked.connect(_prev)
        page_btn_lay.addWidget(prev_btn)

        next_btn = QPushButton("Next")
        next_btn.clicked.connect(_next)
        page_btn_lay.addWidget(next_btn)


    def del_password(self):
        def _delete():
            pass
        layout = QGridLayout()

        layout.setRowStretch(1, 1)
        layout.setRowStretch(99, 1)

        layout.setColumnStretch(1, 3)
        layout.setColumnStretch(3, 2)

        login_lbl = QLabel("Login name:")
        login_lbl.setAlignment(Qt.AlignRight)
        layout.addWidget(login_lbl, 2, 1)

        login_inp = QLineEdit()
        login_inp.setPlaceholderText("example@login.io")
        layout.addWidget(login_inp, 2, 2)

        pass_lbl = QLabel("Password:")
        pass_lbl.setAlignment(Qt.AlignRight)
        layout.addWidget(pass_lbl, 3, 1)

        pass_inp = QLineEdit()
        pass_inp.setEchoMode(QLineEdit.Password)
        pass_inp.setPlaceholderText("password123")
        layout.addWidget(pass_inp, 3, 2)

        sep_lbl = QLabel(" ")
        layout.addWidget(sep_lbl, 6, 1)

        create_btn = QPushButton("Delete")
        create_btn.clicked.connect(_delete)
        layout.addWidget(create_btn, 7, 1, 1, 3)

        self.window = QWidget()
        self.window.setWindowTitle("Delete Password")
        self.window.setLayout(layout)
        self.window.show()

    def initUI(self):
        def _new():
            self.new_password()

        def _upd():
            self.upd_password()

        def _find():
            Utilities.clear_layout(self.screen_lay)
            self.find_password()

        def _del():
            self.del_password()

        def _off():
            Utilities.clear_layout(self.root)
            self.listener()

        main_layout = QVBoxLayout()
        self.root.addLayout(main_layout)

        # | Buttons |

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

        self.screen_lay = QVBoxLayout()
        main_layout.addLayout(self.screen_lay)

        _find()
