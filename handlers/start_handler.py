from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ContextTypes

# -------------------------
# KEYBOARD BUTTONS
# -------------------------
keyboard = [
    ["Merge PDF", "Split PDF"],
    ["Compress PDF", "PDF to Word"],
    ["Word to PDF", "PDF to JPG"],
    ["JPG to PDF", "Feedback/Suggestion"]
]

# -------------------------
# REPLY KEYBOARD
# -------------------------
reply_markup = ReplyKeyboardMarkup(
    keyboard,
    resize_keyboard=True,
    is_persistent=True,
    one_time_keyboard=False
)

# -------------------------
# START COMMAND
# -------------------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    welcome_text = """
🚀 Welcome to RPA Tech Club's Doc Converter

Select a tool from the menu below 👇

📄 Merge PDF
✂️ Split PDF
📦 Compress PDF
🖼 PDF ↔ JPG
📑 Word → PDF

💡 Built by RPA Tech Club
"""

    await update.message.reply_text(
        welcome_text,
        reply_markup=reply_markup
    )