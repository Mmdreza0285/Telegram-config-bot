from aiogram import Router
from aiogram.types import Message
import os

router = Router()
ADMINS = os.getenv("ADMINS", "").split(",")

@router.message(lambda m: str(m.from_user.id) in ADMINS and m.text == "📊 آمار ربات")
async def show_stats(message: Message):
    # اینجا فقط آمار پایه رو میدیم (مثال تعداد اعضا)
    # چون دیتابیس نیست، فقط یه عدد نمونه می‌زنیم
    member_count = 1234  # جایگزین با داده واقعی
    await message.answer(f"📊 آمار ربات:\nتعداد کاربران: {member_count}")
