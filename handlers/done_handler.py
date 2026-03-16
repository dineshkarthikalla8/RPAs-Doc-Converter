from telegram import Update
from telegram.ext import ContextTypes

from config import user_files, user_mode
from functions.merge_pdf import merge_pdf
from functions.image_to_pdf import images_to_pdf

import logging


async def done(update: Update, context: ContextTypes.DEFAULT_TYPE):

    chat_id = update.effective_chat.id
    user = update.effective_user

    if chat_id not in user_mode:
        await update.message.reply_text("⚠️ Select a tool first.")
        return

    mode = user_mode[chat_id]

    logging.info(f"User {user.first_name} ({chat_id}) executed /done for {mode}")

    try:

        # -------------------------
        # MERGE PDF
        # -------------------------
        if mode == "Merge PDF":

            files = user_files.get(chat_id, [])

            if len(files) < 2:
                await update.message.reply_text("❌ Send at least 2 PDF files.")
                return

            await update.message.reply_text("📄 Merging PDFs...")

            await merge_pdf(update, files)

            user_files.pop(chat_id, None)
            user_mode.pop(chat_id, None)

        # -------------------------
        # JPG → PDF
        # -------------------------
        elif mode == "JPG to PDF":

            files = user_files.get(chat_id, [])

            if len(files) == 0:
                await update.message.reply_text("❌ Send images first.")
                return

            await update.message.reply_text("🧾 Creating PDF...")

            await images_to_pdf(update, chat_id, files)

            user_files.pop(chat_id, None)
            user_mode.pop(chat_id, None)

    except Exception as e:

        logging.error(f"Error in /done handler: {e}")

        await update.message.reply_text(
            "❌ Something went wrong while processing your files."
        )