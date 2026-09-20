import os
import subprocess
import shutil


async def word_to_pdf(update, file_path):
    try:
        # Check if LibreOffice is installed
        soffice = shutil.which("soffice")

        if not soffice:
            await update.message.reply_text(
                "❌ Word to PDF conversion is currently unavailable."
            )
            print("ERROR: LibreOffice (soffice) is not installed.")
            return

        # Get directory and filename
        output_dir = os.path.dirname(file_path)
        filename = os.path.splitext(os.path.basename(file_path))[0]
        output = os.path.join(output_dir, filename + ".pdf")

        # Convert DOCX to PDF
        result = subprocess.run(
            [
                soffice,
                "--headless",
                "--convert-to",
                "pdf",
                "--outdir",
                output_dir,
                file_path
            ],
            capture_output=True,
            text=True
        )

        print("LibreOffice stdout:", result.stdout)
        print("LibreOffice stderr:", result.stderr)

        if result.returncode != 0 or not os.path.exists(output):
            await update.message.reply_text(
                "❌ Failed to convert the Word document to PDF."
            )
            return

        # Send converted PDF
        with open(output, "rb") as pdf:
            await update.message.reply_document(
                document=pdf,
                filename=os.path.basename(output)
            )

        # Delete temporary files
        if os.path.exists(file_path):
            os.remove(file_path)

        if os.path.exists(output):
            os.remove(output)

    except Exception as e:
        print("Word to PDF error:", e)
        await update.message.reply_text(
            "❌ An error occurred while converting the document."
        )
