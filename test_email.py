from email_alert import send_email_alert

if __name__ == "__main__":
    send_email_alert(
        subject="Test Email Alert",
        message="This is a test email from your Smart Security System.",
        to_email="mannehajaratou@gmail.com"  # Your email
    )
