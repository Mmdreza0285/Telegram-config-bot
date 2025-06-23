import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
MONGO_URL = os.getenv("MONGO_URL")
ADMINS = [int(admin_id) for admin_id in os.getenv("ADMINS", "").split(",") if admin_id]
CHANNELS = os.getenv("CHANNELS", "").split(",")
