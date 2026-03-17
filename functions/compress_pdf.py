import os
from pdf2image import convert_from_path
from PIL import Image


async def compress_pdf(update, file_path):

    await update.message.reply_text("🔄 Compressing PDF...")

    output = file_path.replace(".pdf", "_compressed.pdf")

    try:

        images = convert_from_path(file_path)

        compressed_images = []

        for img in images:
            img = img.convert("RGB")
            compressed_images.append(img)

        compressed_images[0].save(
            output,
            save_all=True,
            append_images=compressed_images[1:],
            quality=50,   # compression level (lower = smaller file)
            optimize=True
        )

        with open(output, "rb") as f:
            await update.message.reply_document(
                document=f,
                filename="compressed.pdf",
                caption="✅ PDF compressed successfully"
            )

    except Exception as e:
        print("Compression error:", e)
        await update.message.reply_text("❌ Error in compressing your PDF.")

    finally:

        if os.path.exists(file_path):
            os.remove(file_path)

        if os.path.exists(output):
            os.remove(output)