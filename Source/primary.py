from PyQt5 import QtWidgets
from primary_window import Ui_MainWindow

class MainControl(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainControl, self).__init__()
        self.setupUi(self)
        self.switchButton.clicked.connect(self.switch_to_secondary)

    def set_secondary_window(self, secondary_window):
        self.secondary_window = secondary_window

    def switch_to_secondary(self):
        self.secondary_window.show()
        self.close()
