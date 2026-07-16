from telegram import Update
from telegram.ext import ContextTypes
from keyboards.owner import owner_menu
import config

async def owner_login(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Enter Owner Password:")
    context.user_data["waiting_password"] = "owner"

async def owner_panel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text("Owner Panel", reply_markup=owner_menu())

async def toggle_authenticate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    config.AUTHENTICATE_ENABLED = not config.AUTHENTICATE_ENABLED
    query = update.callback_query
    await query.answer("Authenticate Toggled")
    await query.edit_message_reply_markup(reply_markup=owner_menu())
