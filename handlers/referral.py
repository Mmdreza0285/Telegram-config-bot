from aiogram import Router
from aiogram.types import Message
from dotenv import load_dotenv
import os

router = Router()
load_dotenv()
BOT_USERNAME = os.getenv("BOT_USERNAME")  # اگه ندارید باید به .env اضافه کنید یا از API بگیرید

@router.message(lambda m: m.text == "🎁 لینک رفرال")
async def send_referral_link(message: Message):
    user_id = message.from_user.id
    username = BOT_USERNAME if BOT_USERNAME else (await message.bot.get_me()).username
    link = f"https://t.me/{username}?start={user_id}"
    await message.answer(f"🔗 لینک دعوت شما:\n{link}")
