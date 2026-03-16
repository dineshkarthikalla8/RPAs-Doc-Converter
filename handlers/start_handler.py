from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ContextTypes

# Keyboard buttons
keyboard = [
    ["Merge PDF", "Split PDF"],
    ["Compress PDF", "PDF to Word"],
    ["Word to PDF", "PDF to JPG"],["JPG to PDF", "Feedback/Suggestion"]
]

reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)


# Start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📂 RPA DOC CONVERTER\nSelect a tool:",
        reply_markup=reply_markup
    )
