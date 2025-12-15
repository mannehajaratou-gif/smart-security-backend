# whatsapp_alert.py
from twilio.rest import Client

ACCOUNT_SID = os.getenv("TWILIO_API_KEY")
AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_WHATSAPP = os.getenv("WHATSAPP_PHONE_ID")   # Twilio Sandbox number



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
