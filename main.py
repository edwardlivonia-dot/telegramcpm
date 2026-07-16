from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters
import config
from database import engine, Base
import asyncio
from handlers import user, admin, owner, log_management, access_key, redeem

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

def main():
    asyncio.run(init_db())
    app = Application.builder().token(config.BOT_TOKEN).build()
    
    # User
    app.add_handler(CommandHandler("start", user.start))
    # Admin
    app.add_handler(CommandHandler("admincleesmart", admin.admin_login))
    # Owner
    app.add_handler(CommandHandler("ownercleesmart", owner.owner_login))
    
    # Callbacks
    app.add_handler(CallbackQueryHandler(user.menu_accounts, pattern="menu_accounts"))
    app.add_handler(CallbackQueryHandler(owner.owner_panel, pattern="owner_panel"))
    app.add_handler(CallbackQueryHandler(admin.admin_panel, pattern="admin_panel"))
    
    # Redeem + Auth
    app.add_handler(CallbackQueryHandler(owner.toggle_authenticate, pattern="toggle_authenticate"))
    app.add_handler(CallbackQueryHandler(redeem.generate_redeem_final, pattern="^redeem_"))
    
    app.run_polling()

if __name__ == "__main__":
    main()
