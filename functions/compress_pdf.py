import os
import subprocess


async def compress_pdf(update, file_path):

    output = file_path.replace(".pdf", "_compressed.pdf")

    # only one message
    await update.message.reply_text("🔄 Compressing PDF...")

    command = [
        "gs",
        "-sDEVICE=pdfwrite",
        "-dCompatibilityLevel=1.4",
        "-dPDFSETTINGS=/screen",
        "-dNOPAUSE",
        "-dQUIET",
        "-dBATCH",
        f"-sOutputFile={output}",
        file_path
    ]

    subprocess.run(command)

    # ALWAYS send compressed file
    with open(output, "rb") as f:
        await update.message.reply_document(f)

    # cleanup
    if os.path.exists(file_path):
        os.remove(file_path)

    if os.path.exists(output):
        os.remove(output)