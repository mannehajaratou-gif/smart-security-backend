# whatsapp_alert.py
from twilio.rest import Client

ACCOUNT_SID = "AC2132c20624f01b4d8cd2565f88a5551f"
AUTH_TOKEN = "90916f9c0731bdab30f6dfe27a173156"
TWILIO_WHATSAPP = "whatsapp:+14155238886"  # Twilio Sandbox number

client = Client(ACCOUNT_SID, AUTH_TOKEN)

def send_whatsapp_alert(to_number, message):
    try:
        client.messages.create(
            from_=TWILIO_WHATSAPP,
            body=message,
            to=f"whatsapp:{to_number}"
        )
        print("WhatsApp alert sent!")
    except Exception as e:
        print("WhatsApp failed:", e)
