import os
import subprocess


async def compress_pdf(update, file_path):

    output = file_path.replace(".pdf", "_compressed.pdf")

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

    original_size = os.path.getsize(file_path)
    compressed_size = os.path.getsize(output)

    # Send whichever file is smaller
    if compressed_size < original_size:
        send_file = output
        caption = "✅ Compressed PDF"
    else:
        send_file = file_path
        caption = "⚠️ File already optimized. Sending original."

    with open(send_file, "rb") as f:
        await update.message.reply_document(
            document=f,
            caption=caption
        )

    # cleanup
    if os.path.exists(file_path):
        os.remove(file_path)

    if os.path.exists(output):
        os.remove(output)