# email_alert.py
import smtplib
from email.mime.text import MIMEText

EMAIL_ADDRESS = "mannehajaratou@gmail.com"
EMAIL_PASSWORD = "xpglehwkopyvkfcp"

def send_email_alert(subject, message, to_email):
    msg = MIMEText(message)
    msg["Subject"] = subject
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = to_email

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, to_email, msg.as_string())
        
        print("Email alert sent!")
    except Exception as e:
        print("Email failed:", e)
