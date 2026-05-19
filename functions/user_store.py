import json
import os

FILE = "users.json"


# -------------------------
# LOAD USERS
# -------------------------
def load_users():

    if not os.path.exists(FILE):
        return []

    try:
        with open(FILE, "r") as f:
            return json.load(f)

    except:
        return []


# -------------------------
# SAVE USER
# -------------------------
def save_user(user):

    users = load_users()

    # avoid duplicates
    for u in users:
        if u["id"] == user.id:
            return

    users.append({
        "id": user.id,
        "name": user.first_name,
        "username": user.username
    })

    with open(FILE, "w") as f:
        json.dump(users, f, indent=4)


# -------------------------
# GET USERS
# -------------------------
def get_users():
    return load_users()