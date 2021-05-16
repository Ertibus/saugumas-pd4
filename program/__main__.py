import sys
from PyQt5.QtWidgets import QApplication

from program.gui import PyQtGUI

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PyQtGUI()
    sys.exit(app.exec_())
