# upload.py
import io
from datetime import datetime
from supabase_client import supabase

def upload_image(image_bytes, filename):
    filepath = f"{filename}"

    supabase.storage.from_("entries").upload(
        filepath,
        image_bytes,
        {
            "content-type": "image/jpeg",
            "x-upsert": "true"
        }
    )

    signed_url = supabase.storage.from_("entries").create_signed_url(filepath, 604800)
    return signed_url["signedURL"]

def save_log(name, action, image_url):
    now = datetime.utcnow().isoformat()

    supabase.table("Logs").insert({
        "name": name,
        "action": action,
        "image_url": image_url,
        "timestamp": now
    }).execute()
