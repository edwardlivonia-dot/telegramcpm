from telegram import Update
from telegram.ext import ContextTypes
import config

async def check_password(update: Update, context: ContextTypes.DEFAULT_TYPE, role: str):
    if context.user_data.get(f"{role}_auth"):
        return True
    await update.message.reply_text("Enter password:")
    context.user_data["waiting_password"] = role
    return False
