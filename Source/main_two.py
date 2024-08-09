import sys
import cv2
from PyQt6 import QtWidgets, QtGui, QtCore
from new_innovation_screen import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        # self.cameraLabel_2.setPixmap(QtGui.QPixmap("virtual-face.jpg"))
        # Initialize a timer for updating the camera feed
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.cap = cv2.VideoCapture(0)  # Open the default camera
        # self.cap = cv2.VideoCapture("Daisy.mp4")  # Open the default camera

        self.timer.start(30)  # Update the frame every 20 ms

    def update_frame(self):
        ret, frame = self.cap.read()
        if ret:
            # Convert the frame to RGB
            rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # Get image dimensions
            h, w, ch = rgb_image.shape
            bytes_per_line = ch * w
            # Convert to QImage
            qt_image = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format.Format_RGB888)
            # Convert QImage to QPixmap and display
            self.cameraLabel_2.setPixmap(QtGui.QPixmap.fromImage(qt_image))

    def closeEvent(self, event):
        # Release the camera when the window is closed
        self.cap.release()
        super(MainWindow, self).closeEvent(event)

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()