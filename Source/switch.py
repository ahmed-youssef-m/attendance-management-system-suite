import sys
from PyQt5 import QtWidgets
from primary import MainControl
from secondary import SecondaryControl

class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Initialize the main and secondary windows
        self.main_window = MainControl()
        self.secondary_window = SecondaryControl()

        # Set references for switching between windows
        self.main_window.set_secondary_window(self.secondary_window)
        self.secondary_window.set_main_window(self.main_window)

    def run(self):
        self.main_window.show()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my_app = MyApp()
    my_app.run()
    sys.exit(app.exec_())
