from telegram import Update
from telegram.ext import ContextTypes

from config import user_mode
from functions.user_store import save_user

ADMIN_ID = 8162100027


# -------------------------
# FEEDBACK BUTTON
# -------------------------
async def feedback(update: Update, context: ContextTypes.DEFAULT_TYPE):

    chat_id = update.effective_chat.id

    # enable feedback mode
    user_mode[chat_id] = "feedback"

    await update.message.reply_text(
        "✉️ Send your feedback or suggestion."
    )


# -------------------------
# RECEIVE FEEDBACK
# -------------------------
async def receive_feedback(update: Update, context: ContextTypes.DEFAULT_TYPE):

    chat_id = update.effective_chat.id
    text = update.message.text

    # user must be in feedback mode
    if chat_id not in user_mode:
        return

    if user_mode[chat_id] != "feedback":
        return

    user = update.effective_user

    # SAVE USER
    save_user(user)

    # username handling
    if user.username:
        username = f"@{user.username}"
    else:
        username = "No username"

    message = f"""
📩 NEW FEEDBACK

👤 Name: {user.first_name}
📛 Username: {username}
🆔 Telegram ID: {chat_id}

💬 Message:
{text}
"""

    # send feedback to admin
    await context.bot.send_message(
        chat_id=ADMIN_ID,
        text=message
    )

    # reply to user
    await update.message.reply_text(
        "✅ Thank you for your feedback!"
    )

    # remove feedback mode
    user_mode.pop(chat_id, None)