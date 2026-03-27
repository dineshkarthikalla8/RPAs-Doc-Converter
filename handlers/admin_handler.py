from telegram import Update
from telegram.ext import ContextTypes
from config import ADMIN_ID
from functions.user_store import get_users


async def broadcast(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.effective_user.id != ADMIN_ID:
        await update.message.reply_text("❌ Not authorized")
        return

    message = " ".join(context.args)

    if not message:
        await update.message.reply_text("Usage:\n/broadcast your message")
        return

    users = get_users()

    success = 0
    failed = 0

    for user_id in users:
        try:
            await context.bot.send_message(chat_id=user_id, text=message)
            success += 1
        except:
            failed += 1

    await update.message.reply_text(
        f"✅ Sent: {success}\n❌ Failed: {failed}"
    )

async def stats(update, context):

    if update.effective_user.id != ADMIN_ID:
        await update.message.reply_text("❌ Not authorized")
        return

    users = get_users()
    total_users = len(users)

    await update.message.reply_text(
        f"📊 Bot Statistics\n\n👥 Total Users: {total_users}"
    )

async def users_list(update, context):

    if update.effective_user.id != ADMIN_ID:
        return

    users = get_users()

    if not users:
        await update.message.reply_text("No users yet.")
        return

    message = "👥 Users List:\n\n"

    for user in users.values():
        message += f"👤 {user['name']} (@{user['username']})\n🆔 {user['id']}\n\n"

    await update.message.reply_text(message[:4000])  # Telegram limit
