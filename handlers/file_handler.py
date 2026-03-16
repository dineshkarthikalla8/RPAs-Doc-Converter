from telegram import Update
from telegram.ext import ContextTypes

from config import user_files, user_mode
from functions.pdf_to_jpg import pdf_to_jpg
from functions.word_to_pdf import word_to_pdf
from functions.pdf_to_word import pdf_to_word
from functions.compress_pdf import compress_pdf


async def receive_file(update: Update, context: ContextTypes.DEFAULT_TYPE):

    chat_id = update.effective_chat.id

    if chat_id not in user_mode:
        await update.message.reply_text("⚠️ Select a tool first.")
        return

    mode = user_mode[chat_id]

    doc = update.message.document
    photo = update.message.photo

    # -------------------------
    # JPG → PDF (PHOTO)
    # -------------------------
    if mode == "JPG to PDF" and photo:

        file = await photo[-1].get_file()

        save_name = f"{chat_id}_{len(user_files.get(chat_id, []))}.jpg"

        await file.download_to_drive(save_name)

        user_files.setdefault(chat_id, [])
        user_files[chat_id].append(save_name)

        await update.message.reply_text(
            "📸 Image stored.\nSend more images or type /done"
        )

        return

    # -------------------------
    # DOCUMENT HANDLING
    # -------------------------
    if doc:

        filename = doc.file_name.lower()

        file = await doc.get_file()

        save_name = f"{chat_id}_{doc.file_name}"

        await file.download_to_drive(save_name)

        # -------------------------
        # MERGE PDF
        # -------------------------
        if mode == "Merge PDF":

            if not filename.endswith(".pdf"):
                await update.message.reply_text("❌ Only PDF files allowed.")
                return

            user_files.setdefault(chat_id, [])
            user_files[chat_id].append(save_name)

            await update.message.reply_text(
                f"📎 Stored {filename}\nSend more PDFs or type /done"
            )

        # -------------------------
        # SPLIT PDF
        # -------------------------
        elif mode == "Split PDF":

            if not filename.endswith(".pdf"):
                await update.message.reply_text("❌ Send a PDF file.")
                return

            user_files[chat_id] = save_name

            await update.message.reply_text(
                "✂️ Send page range (example: 1-3)"
            )

        # -------------------------
        # PDF → JPG
        # -------------------------
        elif mode == "PDF to JPG":

            if not filename.endswith(".pdf"):
                await update.message.reply_text("❌ Send a PDF file.")
                return

            await pdf_to_jpg(update, save_name)

        # -------------------------
        # WORD → PDF
        # -------------------------
        elif mode == "Word to PDF":

            if not filename.endswith((".doc", ".docx")):
                await update.message.reply_text("❌ Send Word file.")
                return

            await word_to_pdf(update, save_name)

        # -------------------------
        # PDF → WORD
        # -------------------------
        elif mode == "PDF to Word":

            if not filename.endswith(".pdf"):
                await update.message.reply_text("❌ Send a PDF file.")
                return

            await pdf_to_word(update, save_name)

        # -------------------------
        # COMPRESS PDF
        # -------------------------
        elif mode == "Compress PDF":

            if not filename.endswith(".pdf"):
                await update.message.reply_text("❌ Only PDF allowed.")
                return

            await compress_pdf(update, save_name)

    else:
        await update.message.reply_text("❌ Send a valid file.")