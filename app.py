from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json
import os

app = FastAPI()

# Allow React frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

USERS_FILE = "users.json"

# Load users
def load_users():
    if not os.path.exists(USERS_FILE):
        return {}
    with open(USERS_FILE, "r") as f:
        return json.load(f)

# Save users
def save_users(data):
    with open(USERS_FILE, "w") as f:
        json.dump(data, f, indent=4)

@app.post("/register")
def register_user(data: dict):
    users = load_users()
    users[data["name"]] = data["pin"]
    save_users(users)
    return {"message": "User registered successfully"}

@app.get("/logs")
def get_logs():
    return {"logs": ["Camera started", "Face detected", "Alert sent"]}
