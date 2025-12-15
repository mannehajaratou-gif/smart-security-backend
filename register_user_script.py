import face_recognition
from database import register_user

def register_user_with_image():
    print("Register new users. Type 'done' as name to exit.")

    while True:
        name = input("Enter user name: ").strip()
        if name.lower() == "done":
            break

        pin = input("Enter PIN or QR code: ").strip()
        image_path = input("Enter path to face image (e.g., known/username.jpg): ").strip()

        try:
            # Load image and extract face encoding
            user_image = face_recognition.load_image_file(image_path)
            encodings = face_recognition.face_encodings(user_image)

            if not encodings:
                print(f"No face found in image '{image_path}'. Please try again with a clear image.")
                continue

            face_encoding = encodings[0]

            # Register user in database
            success = register_user(name, pin, face_encoding)

            if success:
                print(f"User '{name}' registered successfully.")
            else:
                print(f"Failed to register user '{name}'.")

        except FileNotFoundError:
            print(f"Image file not found: '{image_path}'. Please check the path and try again.")

        except Exception as e:
            print(f"Error processing registration: {e}")

if __name__ == "__main__":
    register_user_with_image()
