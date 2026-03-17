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

    try:
        result = subprocess.run(command, check=True)

        # check if output file created
        if os.path.exists(output):

            with open(output, "rb") as f:
                await update.message.reply_document(
                    document=f,
                    filename="compressed.pdf",
                    caption="✅ Here is your compressed PDF"
                )

        else:
            await update.message.reply_text("❌ Compression failed. Please try again.")

    except Exception as e:
        await update.message.reply_text("❌ Error compressing PDF.")
        print("Compression Error:", e)

    finally:
        # cleanup
        if os.path.exists(file_path):
            os.remove(file_path)

        if os.path.exists(output):
            os.remove(output)