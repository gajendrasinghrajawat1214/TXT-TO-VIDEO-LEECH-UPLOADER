

from os import environ

API_ID = int(environ.get("API_ID", "23065170"))
API_HASH = environ.get("API_HASH", "7d043ca5d09ffc457879b47af9ca77cd")
BOT_TOKEN = environ.get("BOT_TOKEN", "8337571581:AAF9Nn-dyuQ29O4P-fchnWBfpjxKd8tTRqA")

# Force Subscribe Configuration
FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "coursesadda8209")  # Channel username without @, 
FORCE_SUB_CHANNEL_LINK = environ.get("FORCE_SUB_CHANNEL_LINK", "https://t.me/coursesadda8209")  # Channel link

# Admin Configuration
ADMINS = list(map(int, environ.get("ADMINS", "").split()))

# Optional: Bot Owner ID
OWNER_ID = int(environ.get("OWNER_ID", "1211774773"))

# Database URL (if you want to add database support later)
DATABASE_URL = environ.get("DATABASE_URL", "")











