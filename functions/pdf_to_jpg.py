import os
from pdf2image import convert_from_path


async def pdf_to_jpg(update, file_path):

    images = convert_from_path(file_path)

    for i, img in enumerate(images):
        img_name = file_path.replace(".pdf", f"_page_{i+1}.jpg")
        img.save(img_name, "JPEG")

        with open(img_name, "rb") as f:
            await update.message.reply_photo(f)

        os.remove(img_name)

    os.remove(file_path)