from telegram.ext import Application, CommandHandler, MessageHandler, filters

from handlers.start_handler import start
from handlers.menu_handler import menu
from handlers.file_handler import receive_file
from handlers.range_handler import receive_range
from handlers.done_handler import done
from handlers.feedback_handler import receive_feedback

from dotenv import load_dotenv
import os
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

load_dotenv()

# -------------------------
# DUMMY SERVER FOR RAILWAY
# -------------------------
class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot running")


def run_server():
    server = HTTPServer(("0.0.0.0", 8080), Handler)
    server.serve_forever()


threading.Thread(target=run_server, daemon=True).start()

# -------------------------
# TOKEN
# -------------------------
TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    print("❌ BOT_TOKEN missing")

# -------------------------
# APPLICATION
# -------------------------
app = Application.builder().token(TOKEN).build()

# -------------------------
# COMMANDS
# -------------------------
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("done", done))

# -------------------------
# FILE UPLOADS
# -------------------------
app.add_handler(
    MessageHandler(
        filters.Document.ALL | filters.PHOTO,
        receive_file
    )
)

# -------------------------
# SPLIT RANGE
# -------------------------
app.add_handler(
    MessageHandler(
        filters.Regex(r"^\d+-\d+$"),
        receive_range
    )
)

# -------------------------
# MENU BUTTONS
# -------------------------
menu_filter = filters.TEXT & ~filters.COMMAND & filters.Regex(
    r"^(Merge PDF|Split PDF|Compress PDF|PDF to Word|Word to PDF|PDF to JPG|JPG to PDF|Feedback/Suggestion)$"
)

app.add_handler(
    MessageHandler(menu_filter, menu)
)

# -------------------------
# FEEDBACK
# -------------------------
app.add_handler(
    MessageHandler(
        filters.TEXT & ~filters.COMMAND & ~menu_filter,
        receive_feedback
    ),
    group=1
)

print("🚀 Bot Running...")

app.run_polling(drop_pending_updates=True)