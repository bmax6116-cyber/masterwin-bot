import os
import logging
from telegram.ext import Application, CommandHandler

logging.basicConfig(level=logging.INFO)

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise RuntimeError("BOT_TOKEN NON TROVATO")

async def start(update, context):
    await update.message.reply_text("MasterWin ONLINE ✅")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    logging.info("BOT AVVIATO")
    app.run_polling()

if __name__ == "__main__":
    main()
