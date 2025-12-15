# register_user.py
import cv2
import json
import os

DB_FILE = "registered_users/users.json"

def load_db():
    if not os.path.exists(DB_FILE):
        return {}
    with open(DB_FILE, "r") as f:
        return json.load(f)

def save_db(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)

def register_user():
    db = load_db()

    print("=== USER REGISTRATION ===")
    name = input("Enter full name: ").strip()
    pin = input("Enter PIN or QR code: ").strip()

    # Save to DB
    db[name] = {"pin": pin}
    save_db(db)

    # Capture face
    cam = cv2.VideoCapture(0)
    if not cam.isOpened():
        print("Camera not found")
        return

    print("Press ENTER to capture face image...")
    input()

    ret, frame = cam.read()
    if not ret:
        print("Failed to capture.")
        return

    # Save face image
    face_path = f"registered_users/user_faces/{name}.jpg"
    cv2.imwrite(face_path, frame)

    cam.release()

    print("\nUser registered successfully!")
    print(f"Saved face at: {face_path}")
    print(f"Saved PIN in database.")

if __name__ == "__main__":
    register_user()
