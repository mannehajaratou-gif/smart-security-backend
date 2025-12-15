import cv2
import face_recognition
import time
import signal
import sys

from upload import upload_image
from email_alert import send_email_alert
from whatsapp_alert import send_whatsapp_alert
from database import load_known_users, save_log

running = True

def stop_camera(sig, frame):
    global running
    print("Stopping camera safely...")
    running = False

signal.signal(signal.SIGINT, stop_camera)

def start_camera():
    print("Loading known users from database...")
    known_faces, known_names = load_known_users()
    print(f"Loaded {len(known_names)} users.")

    cam = cv2.VideoCapture(0)

    if not cam.isOpened():
        print("Camera not found")
        return

    print("Camera running...")

    while running:
        ret, frame = cam.read()
        if not ret:
            print("Failed to read frame")
            break

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        locations = face_recognition.face_locations(rgb)
        encodings = face_recognition.face_encodings(rgb, locations)

        for encoding in encodings:
            matches = face_recognition.compare_faces(known_faces, encoding)
            name = "Unknown"

            if True in matches:
                name = known_names[matches.index(True)]

            filename = f"capture_{int(time.time())}.jpg"
            _, buffer = cv2.imencode(".jpg", frame)
            url = upload_image(buffer.tobytes(), filename)

            save_log(name, "Face Detected", url)

            if name == "Unknown":
                send_email_alert(
                    "Unknown Face Detected",
                    f"Unknown person detected\n{url}",
                    "mannehajaratou@gmail.com"
                )

            print(f"Detected: {name}")

        time.sleep(1)

    cam.release()
    print("Camera stopped.")

if __name__ == "__main__":
    start_camera()
