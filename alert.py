import smtplib
from email.mime.text import MIMEText

def send_alert(email_to, subject, message):
    email_from = "mannehajaratou@gmail.com"
    app_password = "zteauuipuxdxeyno"

    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = email_from
    msg['To'] = email_to

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(email_from, app_password)
        server.sendmail(email_from, email_to, msg.as_string())
        server.quit()
        print("Alert sent successfully!")
    except Exception as e:
        print("Error sending alert:", e)

# test
send_alert("ajaratoumanneh@gmail.com", "Test Alert", "This is a test message")
