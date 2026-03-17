import os
import subprocess


async def compress_pdf(update, file_path):

    output = file_path.replace(".pdf", "_compressed.pdf")

    await update.message.reply_text("🔄 Compressing PDF...")

    command = [
        "gs",
        "/opt/homebrew/bin/gs",   # <-- replace with your path
        "-sDEVICE=pdfwrite",
        "-dCompatibilityLevel=1.4",
        "-dPDFSETTINGS=/screen",
        "-dNOPAUSE",
        "-dQUIET",
        "-dBATCH",
        f"-sOutputFile={output}",
        file_path
    ]

    try:
        subprocess.run(command, check=True)

        if os.path.exists(output):
            with open(output, "rb") as f:
                await update.message.reply_document(
                    document=f,
                    filename="compressed.pdf",
                    caption="✅ Here is your compressed PDF"
                )
        else:
            await update.message.reply_text("❌ Compression failed.")

    except Exception as e:
        print("Compression Error:", e)
        await update.message.reply_text("❌ Error compressing PDF.")

    finally:
        if os.path.exists(file_path):
            os.remove(file_path)

        if os.path.exists(output):
            os.remove(output)