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
