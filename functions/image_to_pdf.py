from PIL import Image
import os

async def images_to_pdf(update, chat_id, files):

    images = []

    for file in files:
        img = Image.open(file).convert("RGB")
        images.append(img)

    output = f"{chat_id}_images.pdf"

    images[0].save(
        output,
        save_all=True,
        append_images=images[1:]
    )

    with open(output, "rb") as f:
        await update.message.reply_document(f)

    # cleanup
    for file in files:
        if os.path.exists(file):
            os.remove(file)

    if os.path.exists(output):
        os.remove(output)