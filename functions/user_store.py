import json

FILE = "users.json"

def save_user(user_id):
    try:
        with open(FILE, "r") as f:
            users = set(json.load(f))
    except:
        users = set()

    users.add(user_id)

    with open(FILE, "w") as f:
        json.dump(list(users), f)


def get_users():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return []
users = {}

def add_user(user):
    users[user.id] = {
        "id": user.id,
        "name": user.first_name,
        "username": user.username
    }

def get_users():
    return users
