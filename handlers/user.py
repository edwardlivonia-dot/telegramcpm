from telegram import Update
from telegram.ext import ContextTypes
from keyboards.user import user_menu
from keyboards.nav import back_home

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome to CPM Bot\nChoose an option:", 
        reply_markup=user_menu()
    )

async def menu_accounts(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        "📦 CPM Accounts\nFree: 2 orders/day\nPremium: Unlimited", 
        reply_markup=back_home()
    )
