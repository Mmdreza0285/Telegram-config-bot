from aiogram import Router
from aiogram.types import Message

router = Router()

@router.message(lambda m: m.text == "🆘 پشتیبانی")
async def support_start(message: Message):
    await message.answer("📩 پیام خود را ارسال کنید، تیم پشتیبانی به زودی پاسخ می‌دهد.")
