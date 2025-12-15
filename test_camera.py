import cv2

def test_camera():
    cam = cv2.VideoCapture(0)  # Try 0, if not working, try 1 or 2

    if not cam.isOpened():
        print("Cannot open camera")
        return

    print("Camera opened successfully")

    ret, frame = cam.read()
    if not ret:
        print("Failed to capture frame")
    else:
        print("Frame captured successfully")

    cam.release()

if __name__ == "__main__":
    test_camera()
