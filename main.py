import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor
from motor.motor_asyncio import AsyncIOMotorClient

from keyboards import main_menu
from menu import register_menu_handlers
from donate import register_donate_handlers
from utils import is_admin

# ====== Environment Variables ======
BOT_TOKEN = os.environ.get("BOT_TOKEN")
MONGO_URL = os.environ.get("MONGO_URL")
ADMINS = os.environ.get("ADMINS", "").split(",")
CHANNELS = os.environ.get("CHANNELS", "").s
