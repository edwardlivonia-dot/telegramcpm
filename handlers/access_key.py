from telegram import Update
from telegram.ext import ContextTypes

async def generate_access_key(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer("Generating VIP/Premium Key...")
