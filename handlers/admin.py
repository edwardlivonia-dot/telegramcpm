from telegram import Update
from telegram.ext import ContextTypes
from keyboards.admin import admin_menu
import config

async def admin_login(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Enter Admin Password:")
    context.user_data["waiting_password"] = "admin"

async def admin_panel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text("Admin Panel", reply_markup=admin_menu())
