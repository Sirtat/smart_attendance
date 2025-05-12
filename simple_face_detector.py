import cv2
import os
import sqlite3
from datetime import datetime

# Simulated student
simulated_match_name = "Tatenda"  # Change to "Alina" if needed

# Track who’s already been marked this session
marked_present = set()

# Connect to the database
conn = sqlite3.connect("attendance.db")
cursor = conn.cursor()

# Load OpenCV Haar Cascade face detector
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Start webcam
cap = cv2.VideoCapture(0)
print("Webcam started. Press Q to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in faces:
        name = simulated_match_name

        if name not in marked_present:
            marked_present.add(name)
            now = datetime.now()
            date_str = now.strftime("%Y-%m-%d")
            time_str = now.strftime("%H:%M:%S")

            # Save to database
            cursor.execute("INSERT INTO attendance (name, date, time) VALUES (?, ?, ?)",
                           (name, date_str, time_str))
            conn.commit()

            print(f"{date_str} {time_str} - {name} marked present")

        # Draw box and label
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, name, (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2)

    cv2.imshow("Simulated Attendance System", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
conn.close()
