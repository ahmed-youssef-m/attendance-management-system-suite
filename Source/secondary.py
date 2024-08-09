from PyQt5 import QtWidgets
from secondary_window import Ui_SecondaryWindow

class SecondaryControl(QtWidgets.QMainWindow, Ui_SecondaryWindow):
    def __init__(self):
        super(SecondaryControl, self).__init__()
        self.setupUi(self)
        self.backButton.clicked.connect(self.switch_to_main)

    def set_main_window(self, main_window):
        self.main_window = main_window

    def switch_to_main(self):
        self.main_window.show()
        self.close()
