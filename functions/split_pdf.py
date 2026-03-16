from PyPDF2 import PdfReader, PdfWriter
import os
from config import user_files, user_mode


async def split_pdf(update, file_path, page_range):

    chat_id = update.effective_chat.id

    start, end = map(int, page_range.split("-"))

    reader = PdfReader(file_path)
    writer = PdfWriter()

    total_pages = len(reader.pages)

    if start < 1 or end > total_pages:
        await update.message.reply_text("Invalid page range.")
        return

    for i in range(start-1, end):
        writer.add_page(reader.pages[i])

    output_file = f"{chat_id}_split.pdf"

    with open(output_file, "wb") as f:
        writer.write(f)

    await update.message.reply_document(open(output_file, "rb"))

    os.remove(file_path)
    os.remove(output_file)

    user_files.pop(chat_id, None)
    user_mode.pop(chat_id, None)