from pypdf import PdfMerger
import os


async def merge_pdf(update, files):

    merger = PdfMerger()

    for file in files:
        merger.append(file)

    output = f"{files[0].split('_')[0]}_merged.pdf"

    merger.write(output)
    merger.close()

    with open(output, "rb") as f:
        await update.message.reply_document(f)

    # cleanup
    for file in files:
        if os.path.exists(file):
            os.remove(file)

    if os.path.exists(output):
        os.remove(output)