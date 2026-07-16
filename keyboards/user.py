from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def user_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📦 CPM Accounts", callback_data="menu_accounts")],
        [InlineKeyboardButton("💰 Wallet", callback_data="wallet")],
        [InlineKeyboardButton("🎟 Redeem Code", callback_data="redeem_code")],
        [InlineKeyboardButton("📞 Support", callback_data="support")]
    ])
