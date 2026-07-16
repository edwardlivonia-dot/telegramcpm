from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def admin_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📤 Upload Logs", callback_data="upload_logs")],
        [InlineKeyboardButton("📊 View Stats", callback_data="stats")],
        [InlineKeyboardButton("👥 Users", callback_data="users")],
        [InlineKeyboardButton("📢 Complaints", callback_data="complaints")],
        [InlineKeyboardButton("🔙 Back", callback_data="back"), 
         InlineKeyboardButton("🏠 Home", callback_data="home")]
    ])
