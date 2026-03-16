import os
from pdf2docx import Converter


async def pdf_to_word(update, file_path):

    output = file_path.replace(".pdf", ".docx")

    cv = Converter(file_path)
    cv.convert(output)
    cv.close()

    with open(output, "rb") as f:
        await update.message.reply_document(f)

    os.remove(file_path)
    os.remove(output)