import os
from config import user_files

def cleanup(chat_id, output):

    for f in user_files[chat_id]:
        if os.path.exists(f):
            os.remove(f)

    if os.path.exists(output):
        os.remove(output)

    user_files[chat_id] = []
