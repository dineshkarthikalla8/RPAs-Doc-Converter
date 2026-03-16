from telegram import Update
from telegram.ext import ContextTypes
from config import user_mode, user_files
from handlers.feedback_handler import feedback


async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):

    chat_id = update.effective_chat.id
    text = update.message.text

    # MERGE PDF
    if text == "Merge PDF":
        user_mode[chat_id] = "Merge PDF"
        user_files[chat_id] = []

        await update.message.reply_text(
            "📎 Send PDF files one by one.\nThen type /done"
        )

    # WORD TO PDF
    elif text == "Word to PDF":
        user_mode[chat_id] = "Word to PDF"

        await update.message.reply_text(
            "📎 Send Word (.docx) file."
        )

    # SPLIT PDF
    elif text == "Split PDF":
        user_mode[chat_id] = "Split PDF"

        await update.message.reply_text(
            "📎 Send a PDF file to split."
        )

    # PDF TO JPG
    elif text == "PDF to JPG":
        user_mode[chat_id] = "PDF to JPG"

        await update.message.reply_text(
            "📎 Send a PDF file."
        )

    # COMPRESS PDF
    elif text == "Compress PDF":
        user_mode[chat_id] = "Compress PDF"

        await update.message.reply_text(
            "📎 Send a PDF file to compress."
        )

    # PDF TO WORD
    elif text == "PDF to Word":
        user_mode[chat_id] = "PDF to Word"

        await update.message.reply_text(
            "📎 Send a PDF file."
        )

    # JPG TO PDF
    elif text == "JPG to PDF":
        user_mode[chat_id] = "JPG to PDF"
        user_files[chat_id] = []

        await update.message.reply_text(
            "📸 Send JPG images one by one.\nThen type /done"
        )

    # FEEDBACK
    elif text == "Feedback/Suggestion":
        await feedback(update, context)