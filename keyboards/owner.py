from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import config

def owner_menu():
    auth_text = "🟢 ON" if config.AUTHENTICATE_ENABLED else "🔴 OFF"
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🔑 Access Keys", callback_data="access_keys")],
        [InlineKeyboardButton("🎟 Redeem Codes", callback_data="redeem_codes")],
        [InlineKeyboardButton("📁 Log Management", callback_data="log_management")],
        [InlineKeyboardButton(f"🔐 Authenticate: {auth_text}", callback_data="toggle_authenticate")],
        [InlineKeyboardButton("⚙️ Bot Settings", callback_data="bot_settings")],
        [InlineKeyboardButton("🔙 Back", callback_data="back"), 
         InlineKeyboardButton("🏠 Home", callback_data="home")]
    ])
