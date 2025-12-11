import os
import wikipediaapi
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("8299291699:AAE3QMvrCWLCQvpiASATDUmYEJsf1BxSxmc")

wiki = wikipediaapi.Wikipedia(
    user_agent='DiyorbekWikiBot/1.0 (contact: thenarimonov@gmail.com)',
    language='en'
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salom! Wikipedia botiga xush kelibsiz!\nQidiruv so‘zini yuboring.\nFaqat ingilis tilida!")

async def search(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.message.text
    page = wiki.page(query)

    if not page.exists():
        await update.message.reply_text("Topilmadi ❌")
        return

    summary = page.summary[:1000]
    await update.message.reply_text(summary)

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT, search))
    app.run_polling()

if __name__ == "__main__":
    main()
