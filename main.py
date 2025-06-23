from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor
from motor.motor_asyncio import AsyncIOMotorClient

from config import BOT_TOKEN, MONGO_URL, ADMINS, CHANNELS
from keyboards import main_menu
from menu import register_menu_handlers
from donate import register_donate_handlers
from utils import is_admin

# ====== Bot & Dispatcher Setup ======
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# ====== Database Setup ======
client = AsyncIOMotorClient(MONGO_URL)
db = client["shadowvpn"]
users_col = db["users"]

# ====== Start Command ======
@dp.message_handler(commands=["start"])
async def start_handler(message: Message):
    user_id = str(message.from_user.id)

    # ثبت کاربر جدید در دیتابیس
    if not await users_col.find_one({"_id": user_id}):
        await users_col.insert_one({
            "_id": user_id,
            "username": message.from_user.username or "",
            "referrals": [],
        })

    await message.answer("سلام خوش اومدی 😊", reply_markup=main_menu())

# ====== ثبت همه هندلرها ======
register_menu_handlers(dp, db)
register_donate_handlers(dp)

# ====== اجرای ربات ======
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
