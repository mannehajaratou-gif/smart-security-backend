import cv2
import face_recognition
import numpy as np
import json
from database import load_known_users, save_log
from supabase_client import supabase

def recognize_faces():
    print("Loading users from database...")
    known_encodings, known_names = load_known_users()

    if not known_encodings:
        print("No registered users found. Add users first.")
        return

    known_encodings = np.array(known_encodings)

    video = cv2.VideoCapture(0)

    print("Camera started. Press 'q' to exit.")

    while True:
        ret, frame = video.read()
        if not ret:
            print("Camera error.")
            break

        rgb_frame = frame[:, :, ::-1]

        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        for face_encoding, (top, right, bottom, left) in zip(face_encodings, face_locations):
            distances = face_recognition.face_distance(known_encodings, face_encoding)
            match_index = np.argmin(distances)

            if distances[match_index] < 0.45:  
                name = known_names[match_index]
                color = (0, 255, 0)
                label = f"{name}"
                save_log(name, "authorized", "")
            else:
                name = "UNKNOWN"
                color = (0, 0, 255)
                label = "UNKNOWN"
                save_log("UNKNOWN", "unauthorized", "")

            cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
            cv2.putText(frame, label, (left, top - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)

        cv2.imshow("Smart Security System", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    recognize_faces()
