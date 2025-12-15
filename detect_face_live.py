import cv2
import face_recognition
import numpy as np
import datetime
from database import load_known_users, save_log


def detect_faces_live():
    print("\nStarting live detection... Press Q to quit.\n")

    known_encodings, known_names = load_known_users()

    if not known_encodings:
        print("No registered users found! Please register at least one user first.")
        return

    video = cv2.VideoCapture(0)

    while True:
        ret, frame = video.read()
        if not ret:
            print("Failed to access camera.")
            break

        rgb_frame = frame[:, :, 2::-1]

        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        for encoding, location in zip(face_encodings, face_locations):
            matches = face_recognition.compare_faces(known_encodings, encoding)
            name = "Unknown"

            if True in matches:
                index = matches.index(True)
                name = known_names[index]

            # Draw a box around the face
            top, right, bottom, left = location
            color = (0, 255, 0) if name != "Unknown" else (0, 0, 255)
            cv2.rectangle(frame, (left, top), (right, bottom), color, 2)

            # Write name
            cv2.putText(frame, name, (left, top - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

            # Save the log
            timestamp = datetime.datetime.utcnow().isoformat()

            save_log(name, "detected", "image_url_later")

        cv2.imshow("Smart Security Camera", frame)

        # Quit with Q
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    video.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    detect_faces_live()
