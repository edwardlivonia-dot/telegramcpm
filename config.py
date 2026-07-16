import os
from dotenv import load_dotenv
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
OWNER_ID = int(os.getenv("OWNER_ID", 5980762931))
ADMIN_IDS = [int(x) for x in os.getenv("ADMIN_IDS", "").split(",") if x]
DATABASE_URL = os.getenv("DATABASE_URL")
AUTHENTICATE_ENABLED = os.getenv("AUTHENTICATE_ENABLED", "false") == "true"
ADMIN_PASSWORD = "21210"
DAILY_FREE_LIMIT = 2
LIMIT_COST = 500
