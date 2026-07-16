from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def back_home():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🔙 Back", callback_data="back"), 
         InlineKeyboardButton("🏠 Home", callback_data="home")]
    ])

def refresh():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🔄 Refresh", callback_data="refresh")],
        [InlineKeyboardButton("🔙 Back", callback_data="back"), 
         InlineKeyboardButton("🏠 Home", callback_data="home")]
    ])
