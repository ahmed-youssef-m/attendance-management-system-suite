import sys
import os
import cv2
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QMainWindow
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QTimer

# Load face recognition model and data
people = [name for name in os.listdir('../Resources/Faces') if os.path.isdir(os.path.join('../Resources/Faces', name))]
face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read('../Resources/Models/face_trained_model.yml')
CONFIDENCE_THRESHOLD = 30

class VideoDisplayWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Video Display")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Create a QLabel to display the video frame
        self.image_label = QLabel()
        self.layout.addWidget(self.image_label)

        # Initialize video capture
        self.cap = cv2.VideoCapture(0)  # Change to video file path if needed

        # Setup timer to trigger the display update
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_image)
        self.timer.start(33)  # Update at 30 FPS (33 milliseconds per frame)

    def recognize_face(self, faces_roi):
        """
        Recognizes faces in the given region of interest (ROI).
        """
        label, confidence = face_recognizer.predict(faces_roi)
        if confidence < CONFIDENCE_THRESHOLD:
            return label, confidence  # Recognized as a known person
        else:
            return -1, confidence  # Recognized as unknown (-1 label)

    def update_image(self):
        """
        Continuously reads frames from the video capture, performs face recognition,
        and updates the label with the annotated frame.
        """
        ret, frame = self.cap.read()

        if not ret:
            print("Error: Unable to capture frame")
            return

        # Convert BGR (OpenCV format) to RGB (PyQt format)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Detect faces using Haar cascade
        gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        haar_cascade = cv2.CascadeClassifier('../Resources/Models/haar_face.xml')
        faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

        # Process each detected face
        for (x, y, w, h) in faces_rect:
            faces_roi = gray[y:y + h, x:x + w]
            label, confidence = self.recognize_face(faces_roi)

            if label != -1:
                person_name = people[label]
                confidence_percent = f"{round(100 - confidence)}%"
                label_text = f"{person_name} ({confidence_percent} confidence)"
            else:
                label_text = f"Unknown ({round(confidence)}% confidence)"

            # Draw label and rectangle around the face
            cv2.putText(frame, label_text, (x, y - 10), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 0), thickness=1)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), thickness=1)

        # Create QImage from frame data
        height, width, channel = frame.shape
        bytes_per_line = 3 * width
        qimg = QImage(frame.data, width, height, bytes_per_line, QImage.Format_RGB888)

        # Convert QImage to QPixmap and display on the label
        pixmap = QPixmap.fromImage(qimg)
        self.image_label.setPixmap(pixmap)

    def closeEvent(self, event):
        """
        Cleanup resources when the widget is closed.
        """
        self.cap.release()  # Release the video capture
        self.timer.stop()   # Stop the timer
        event.accept()

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.widget = VideoDisplayWidget()  # Create the widget
        self.setCentralWidget(self.widget)  # Set it as central widget

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Create the video display widget
    widget = MyWindow()
    widget.show()

    sys.exit(app.exec_())
