import os
from pypdf import PdfReader, PdfWriter


async def compress_pdf(update, file_path):

    output = file_path.replace(".pdf", "_compressed.pdf")

    await update.message.reply_text("🔄 Compressing PDF...")

    try:

        reader = PdfReader(file_path)
        writer = PdfWriter()

        for page in reader.pages:
            page.compress_content_streams()
            writer.add_page(page)

        with open(output, "wb") as f:
            writer.write(f)

        with open(output, "rb") as f:
            await update.message.reply_document(
                document=f,
                filename="compressed.pdf",
                caption="✅ Here is your compressed PDF"
            )

    except Exception as e:
        print("Compression Error:", e)
        await update.message.reply_text("❌ Error compressing PDF.")

    finally:

        if os.path.exists(file_path):
            os.remove(file_path)

        if os.path.exists(output):
            os.remove(output)