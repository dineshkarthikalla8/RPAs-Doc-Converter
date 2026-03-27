from telegram import Update
from telegram.ext import ContextTypes
from config import user_mode
from functions.user_store import save_user   # ✅ ADD THIS

ADMIN_ID = 8162100027


async def feedback(update: Update, context: ContextTypes.DEFAULT_TYPE):

    chat_id = update.effective_chat.id

    # set feedback mode
    user_mode[chat_id] = "feedback"

    await update.message.reply_text(
        "✉️ Send your feedback or suggestion."
    )


async def receive_feedback(update: Update, context: ContextTypes.DEFAULT_TYPE):

    chat_id = update.effective_chat.id
    text = update.message.text

    if chat_id not in user_mode:
        return

    if user_mode[chat_id] != "feedback":
        return

    user = update.effective_user

    # ✅ ADD THIS (VERY IMPORTANT)
    save_user(chat_id)

    message = f"""
📩 New Feedback

👤 User: {user.first_name}
🆔 ID: {chat_id}

💬 Message:
{text}
"""

    # send feedback to admin
    await context.bot.send_message(
        chat_id=ADMIN_ID,
        text=message
    )

    await update.message.reply_text(
        "✅ Thank you for your feedback!"
    )

    # exit feedback mode
    user_mode.pop(chat_id, None)
