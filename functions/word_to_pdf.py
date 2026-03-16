import subprocess


async def word_to_pdf(update, file_path):

    subprocess.run([
        "soffice",
        "--headless",
        "--convert-to",
        "pdf",
        file_path
    ])

    output = file_path.replace(".docx", ".pdf")

    await update.message.reply_document(open(output, "rb"))