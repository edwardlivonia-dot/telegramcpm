from telegram import Update
from telegram.ext import ContextTypes
from keyboards.nav import refresh

async def log_management(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        "📁 Log Management\nView | Edit | Delete | Move", 
        reply_markup=refresh()
    )
