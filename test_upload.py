from upload import upload_image, save_Log

# Fake image to test upload
with open("test.jpg", "rb") as f:
    image_bytes = f.read()

url = upload_image(image_bytes, "test.jpg")
print("Uploaded image URL:", url)

save_Log("Test User", "PIN", url)
print("Log saved")
