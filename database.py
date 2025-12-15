from supabase_client import supabase
import json
import numpy as np
from datetime import datetime

def load_known_users():
    response = supabase.table("users").select("*").execute()

    users = response.data
    known_encodings = []
    known_names = []

    for user in users:
        encoding = np.array(json.loads(user["face_encoding"]))
        known_encodings.append(encoding)
        known_names.append(user["name"])

    return known_encodings, known_names


def save_log(name, action, image_url):
    data = {
        "name": name,
        "action": action,
        "image_url": image_url,
        "timestamp": datetime.utcnow().isoformat()
    }
    response = supabase.table("Logs").insert(data).execute()
    print("Log saved:", response)
def load_logs():
    response = supabase.table("Logs").select("*").order("timestamp", desc=True).execute()
    return response.data
