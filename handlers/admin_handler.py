from telegram import Update
from telegram.ext import ContextTypes

from config import ADMIN_ID
from functions.user_store import get_users


# -------------------------
# USERS LIST
# -------------------------
async def users_list(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.effective_user.id != ADMIN_ID:
        return

    users = get_users()

    if not users:
        await update.message.reply_text("No users yet.")
        return

    message = "👥 USERS LIST\n\n"

    for user in users:

        username = user.get("username")

        if username:
            username_text = f"@{username}"
        else:
            username_text = "No username"

        message += (
            f"👤 {user['name']} ({username_text})\n"
            f"🆔 {user['id']}\n\n"
        )

    await update.message.reply_text(message[:4000])


# -------------------------
# STATS
# -------------------------
async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.effective_user.id != ADMIN_ID:
        return

    users = get_users()

    total_users = len(users)

    text = f"""
📊 BOT STATISTICS

👥 Total Users: {total_users}

🚀 RPA Tech Club's Doc Converter
"""

    await update.message.reply_text(text)


# -------------------------
# BROADCAST
# -------------------------
async def broadcast(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.effective_user.id != ADMIN_ID:
        return

    message = " ".join(context.args)

    if not message:
        await update.message.reply_text(
            "Usage:\n/broadcast your message"
        )
        return

    users = get_users()

    success = 0
    failed = 0

    for user in users:

        try:
            await context.bot.send_message(
                chat_id=user["id"],
                text=f"📢 ADMIN MESSAGE\n\n{message}"
            )

            success += 1

        except:
            failed += 1

    await update.message.reply_text(
        f"✅ Sent: {success}\n❌ Failed: {failed}"
    )