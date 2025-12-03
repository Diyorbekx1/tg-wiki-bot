import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
import wikipediaapi

TOKEN = os.environ.get("TELEGRAM_TOKEN")

wiki = wikipediaapi.Wikipedia(
    user_agent='DiyorbekWikipediaBot/1.0 (t.me/wikipediabydiorbot)',
    language='en'
)

async def start(update: Update, context):
    await update.message.reply_text("Salom! Menga Wikipedia haqida so‘rov yozing.")

async def handle_message(update: Update, context):
    query = update.message.text
    page = wiki.page(query)

    if page.exists():
        summary = page.summary[:1500]
        await update.message.reply_text(summary)
    else:
        await update.message.reply_text("Bu mavzu topilmadi.")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, handle_message))

app.run_polling()
