from telegram import Update
from telegram.ext import ContextTypes
from config import user_mode, user_files
from functions.split_pdf import split_pdf

import logging


async def receive_range(update: Update, context: ContextTypes.DEFAULT_TYPE):

    chat_id = update.effective_chat.id
    text = update.message.text

    if chat_id not in user_mode:
        return

    if user_mode[chat_id] != "Split PDF":
        return

    if chat_id not in user_files:
        await update.message.reply_text("Upload a PDF first.")
        return

    file_path = user_files[chat_id]

    logging.info(f"User {chat_id} requested split range: {text}")

    await split_pdf(update, file_path, text)

    # cleanup after splitting
    del user_files[chat_id]