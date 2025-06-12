
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Salom! Men Aqiltop botman. Savolingiz bormi?")

if __name__ == '__main__':
    application = ApplicationBuilder().token("YOUR_BOT_TOKEN_HERE").build()
    application.add_handler(CommandHandler("start", start))
    application.run_polling()
