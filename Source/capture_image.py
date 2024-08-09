import os

import cv2

people = [name for name in os.listdir('../Resources/Faces') if os.path.isdir(os.path.join('../Resources/Faces', name))]
count1=0
def capture_image(camera_index):
    cap = cv2.VideoCapture(camera_index)
    count=0
    cv2.namedWindow('Video', cv2.WINDOW_NORMAL)  # Create a resizable window
    cv2.resizeWindow('Video', 600, 600)  # Set initial window size
    while count<15:
        if not cap.isOpened():
            print("Error: Could not open camera.")
            return

        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture image")
            cap.release()
            return

        cv2.imshow('Video', frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        if key == ord('s'):
            cv2.imwrite(f'../Resources/Faces/{people[count1]}/{count}.jpg', frame)
            print(f"Image captured and saved to {count}")
            count+=1

    cap.release()
    cv2.destroyAllWindows()


while count1<len(people):
    capture_image(f'../Resources/Faces/{people[count1]}.mp4')
    count1+=1
