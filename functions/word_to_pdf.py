import os
import shutil
import subprocess


async def word_to_pdf(update, file_path):
    try:
        soffice = shutil.which("soffice")

        if not soffice:
            print("ERROR: soffice not found")
            await update.message.reply_text(
                "❌ Word to PDF conversion is currently unavailable."
            )
            return

        output_dir = os.path.dirname(file_path)
        filename = os.path.splitext(os.path.basename(file_path))[0]
        output = os.path.join(output_dir, filename + ".pdf")

        result = subprocess.run(
            [
                soffice,
                "--headless",
                "--convert-to", "pdf",
                "--outdir", output_dir,
                file_path
            ],
            capture_output=True,
            text=True
        )

        print("STDOUT:", result.stdout)
        print("STDERR:", result.stderr)

        if result.returncode != 0 or not os.path.exists(output):
            await update.message.reply_text(
                "❌ Failed to convert Word document to PDF."
            )
            return

        with open(output, "rb") as pdf:
            await update.message.reply_document(
                document=pdf,
                filename=os.path.basename(output)
            )

        os.remove(file_path)
        os.remove(output)

    except Exception as e:
        print("Word to PDF error:", e)
        await update.message.reply_text(
            "❌ Error converting Word document to PDF."
        )
