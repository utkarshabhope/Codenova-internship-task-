 import cv2
import csv
from datetime import datetime

# Load face detection model
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# Start webcam
cap = cv2.VideoCapture(0)

name = input("Enter your name: ")

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)

        # Save attendance
        with open("attendance.csv", "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([name, datetime.now()])

        print("Attendance Marked!")
        cap.release()
        cv2.destroyAllWindows()
        exit()

    cv2.imshow("Face Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()