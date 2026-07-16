from telegram import Update
from telegram.ext import ContextTypes

async def generate_redeem_final(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    data = query.data # redeem_wallet_500 or redeem_limit_1
    await query.answer("Redeem Code Generated")
