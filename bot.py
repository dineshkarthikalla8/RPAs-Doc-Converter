from telegram.ext import Application, CommandHandler, MessageHandler, filters

from handlers.start_handler import start
from handlers.menu_handler import menu
from handlers.file_handler import receive_file
from handlers.range_handler import receive_range
from handlers.done_handler import done
from handlers.feedback_handler import feedback, receive_feedback

TOKEN = open("token.txt").read().strip()

app = Application.builder().token(TOKEN).build()

# -------------------------
# COMMANDS
# -------------------------
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("done", done))

# -------------------------
# FILE UPLOADS (PDF, WORD, IMAGES)
# -------------------------
app.add_handler(MessageHandler(filters.Document.ALL | filters.PHOTO, receive_file))

# -------------------------
# SPLIT RANGE
# -------------------------
app.add_handler(MessageHandler(filters.Regex(r"^\d+-\d+$"), receive_range))


# -------------------------
# MENU BUTTONS
# -------------------------
menu_filter = filters.TEXT & ~filters.COMMAND & filters.Regex(
    r"^(Merge PDF|Split PDF|Compress PDF|PDF to Word|Word to PDF|PDF to JPG|JPG to PDF|Feedback/Suggestion)$"
)

app.add_handler(MessageHandler(menu_filter, menu))


# -------------------------
# FEEDBACK MESSAGES
# -------------------------
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, receive_feedback))


print("Bot Running...")
app.run_polling()