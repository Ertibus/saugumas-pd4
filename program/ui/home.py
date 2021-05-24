from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.Qt import QRect

import os

from program.utils import Utilities
from program.filemg import FileMG

class Popup(QWidget):
    def __init__(self, btn_name:str, btn_func):
        QWidget.__init__(self)
        self.btn_name = btn_name
        self.btn_func = btn_func
        self.setWindowTitle(self.btn_name + " password")

        self.initUI()
    
    def initUI(self):
        def __button_press():
            self.btn_func(login_inp.text(), pass_inp.text(), url_inp.text(), desc_inp.text())
            self.close()

        def __generate_password():
            gen_pass = os.urandom(8).hex()
            
            pass_inp.setText(gen_pass)

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

        pass_lay = QHBoxLayout()
        layout.addLayout(pass_lay, 3, 2)

        pass_inp = QLineEdit()
        pass_inp.setPlaceholderText("password123")
        pass_lay.addWidget(pass_inp)

        gener_btn = QPushButton("gen")
        gener_btn.clicked.connect(__generate_password)
        pass_lay.addWidget(gener_btn)

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
        create_btn.clicked.connect(__button_press)
        layout.addWidget(create_btn, 7, 1, 1, 3)

class Home():
    def __init__(self, root, listener, uid):
        self.root = root
        self.initUI()
        self.uid = uid
        self.listener = listener

    def new_password(self):
        def _create(login:str, password:str, appurl:str, desc:str):
            try:
                FileMG.new_password(login, password, appurl, desc)
            except Exception as err:
                print(err)
            else:
                Utilities.clear_layout(self.screen_lay)
                self.find_password()

        self.popup = Popup("Create", _create)
        self.popup.show()

    def upd_password(self):
        def _update(login:str, password:str, appurl:str, desc:str):
            FileMG.update_password(login, password, appurl, desc)
            Utilities.clear_layout(self.screen_lay)
            self.find_password()
        self.popup = Popup("Update", _update)
        self.popup.show()

    def find_password(self):
        def _search():
            self.entry_arr = FileMG.get_search_results(login_inp.text())
            _draw_list()

        def _next():
            self.entry_id += 1
            if len(self.entry_arr) < self.entry_id * 10 - 1:
                self.entry_id = len(self.entry_arr) - 11
                if self.entry_id < 0:
                    self.entry_id = 0
            _draw_list()

        def _prev():
            self.entry_id -= 1
            if self.entry_id < 0:
                self.entry_id = 0
            _draw_list()

        def _draw_list():
            def _show_pass(entry, en_pass):
                entry.setText(FileMG.show_password(en_pass))

            def _copy_pass(passwo):
                Utilities.copy_clip(FileMG.show_password(passwo))

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

            for i in range(1, 11):
                if i - 1 + self.entry_id >= len(self.entry_arr):
                    break;
                curr_entry = self.entry_arr[i - 1 + self.entry_id]
                if curr_entry[0].isspace() or not curr_entry[0]:
                    continue

                login_inp = QLineEdit(curr_entry[0])
                login_inp.setReadOnly(True)
                entry_layout.addWidget(login_inp, i, 0)

                pass_inp = QLineEdit(curr_entry[1])
                pass_inp.setReadOnly(True)
                entry_layout.addWidget(pass_inp, i, 1)

                show_btn = QPushButton("*")
                show_btn.clicked.connect(lambda state, entry=pass_inp, password=curr_entry[1]: _show_pass(entry, password))
                entry_layout.addWidget(show_btn, i, 2)

                copy_btn = QPushButton("Copy")
                copy_btn.clicked.connect(lambda state, password=curr_entry[1]: _copy_pass(password))
                entry_layout.addWidget(copy_btn, i, 3)

                url_inp = QLineEdit(curr_entry[2])
                url_inp.setReadOnly(True)
                entry_layout.addWidget(url_inp, i, 4)

                desc_inp = QLineEdit(curr_entry[3])
                desc_inp.setReadOnly(True)
                entry_layout.addWidget(desc_inp, i, 5)


        self.entry_id = 0
        self.entry_arr = FileMG.get_all_passwords()

        layout = QGridLayout()
        self.screen_lay.addLayout(layout)

        layout.setRowStretch(5, 1)

        layout.setColumnStretch(2, 1)


        sep_lbl = QLabel(" ")
        layout.addWidget(sep_lbl, 1, 1)

        login_lbl = QLabel("Login name:")
        login_lbl.setAlignment(Qt.AlignRight)
        layout.addWidget(login_lbl, 2, 1)

        login_inp = QLineEdit()
        login_inp.setPlaceholderText("example@login.io")
        layout.addWidget(login_inp, 2, 2,)

        search_btn = QPushButton("Search")
        search_btn.clicked.connect(_search)
        layout.addWidget(search_btn, 2, 3,)

        sep_lbl = QLabel(" ")
        layout.addWidget(sep_lbl, 3, 1)


        entry_layout = QGridLayout()
        entry_layout.setColumnStretch(1, 1)
        entry_layout.setColumnStretch(5, 1)

        entry_group = QGroupBox("Password list:")
        entry_group.setLayout(entry_layout)
        layout.addWidget(entry_group, 4, 1, 1, 4)

        _draw_list()

        page_btn_lay = QHBoxLayout()
        layout.addLayout(page_btn_lay, 6, 1, 1, 3)

        page_btn_lay.addStretch()

        prev_btn = QPushButton("Prev")
        prev_btn.clicked.connect(_prev)
        page_btn_lay.addWidget(prev_btn)

        next_btn = QPushButton("Next")
        next_btn.clicked.connect(_next)
        page_btn_lay.addWidget(next_btn)


    def del_password(self):
        def _delete():
            FileMG.delete_password(login_inp.text())
            self.window.close()
            Utilities.clear_layout(self.screen_lay)
            self.find_password()

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
