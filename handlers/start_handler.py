from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ContextTypes
from functions.user_store import save_user   # 👈 ADD THIS
from functions.user_store import add_user


keyboard = [
    ["Merge PDF", "Split PDF"],
    ["Compress PDF", "PDF to Word"],
    ["Word to PDF", "PDF to JPG"],
    ["JPG to PDF", "Feedback/Suggestion"]
]

reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    user_id = update.effective_user.id
    save_user(user_id)   # 👈 STORE USER

    await update.message.reply_text(
        "📂 RPA DOC CONVERTER\nSelect a tool:",
        reply_markup=reply_markup
    )
async def start(update, context):
    user = update.effective_user
    add_user(user)

    await update.message.reply_text("Welcome to DOC Converter Bot 🚀")
