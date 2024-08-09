import os

import cv2

people = [name for name in os.listdir('../Resources/Faces') if os.path.isdir(os.path.join('../Resources/Faces', name))]
face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read('../Resources/Models/face_trained_model.yml')

CONFIDENCE_THRESHOLD = 30
def recognize_face(faces_roi):
    label, confidence = face_recognizer.predict(faces_roi)

    if confidence < CONFIDENCE_THRESHOLD:
        return label, confidence  # Recognized as a known person
    else:
        return -1, confidence  # Recognized as unknown (-1 label)


def capture_frames():
    # cap = cv2.VideoCapture('3029.mp4')
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    try:
        cv2.namedWindow('Frame', cv2.WINDOW_NORMAL)  # Create a resizable window
        cv2.resizeWindow('Frame', 600, 600)  # Set initial window size

        while True:
            ret, frame = cap.read()
            if not ret:
                print("Error: Failed to capture frame.")
                break

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            haar_cascade = cv2.CascadeClassifier('../Resources/Models/haar_face.xml')
            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
            for (x, y, w, h) in faces_rect:
                faces_roi = gray[y:y + h, x:x + w]
                label, confidence = recognize_face(faces_roi)
                if label != -1:
                    person_name = people[label]
                    confidence_percent = f"{round(100 - confidence)}%"
                    label_text = f"{person_name} ({confidence_percent} confidence)"
                else:
                    label_text = f"Unknown ({round(confidence)}% confidence)"

                cv2.putText(frame, label_text, (20, 20), cv2.FONT_HERSHEY_COMPLEX, 1.0, (0, 255, 0), thickness=2)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)

            cv2.imshow('Frame', frame)
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                break

    finally:
        cap.release()
        cv2.destroyAllWindows()

capture_frames()
