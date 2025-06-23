from aiogram import Router
from aiogram.types import Message
import os

router = Router()
ADMINS = os.getenv("ADMINS", "").split(",")

# متن و دکمه‌های منو بصورت دیکشنری ذخیره میشن که ادمین میتونه تغییر بده
menu_texts = {
    "main_menu": "به ربات خوش آمدید! یکی از گزینه‌ها را انتخاب کنید:",
    "free_servers": "📡 دریافت سرور رایگان",
    "donate": "📬 اهدا سرور",
    "referral": "🎁 لینک رفرال",
    "support": "🆘 پشتیبانی",
    "admin_panel": "🛠 پنل مدیریت",
    "stats": "📊 آمار ربات",
}

@router.message(lambda m: str(m.from_user.id) in ADMINS and m.text and m.text.startswith("/editmenu "))
async def edit_menu_text(message: Message):
    # دستور: /editmenu کلید متن جدید
    parts = message.text.split(" ", 2)
    if len(parts) < 3:
        await message.answer("❌ دستور صحیح: /editmenu کلید متن جدید")
        return
    key = parts[1]
    new_text = parts[2]

    if key not in menu_texts:
        await message.answer(f"❌ کلید {key} یافت نشد.")
        return

    menu_texts[key] = new_text
    await message.answer(f"✅ متن کلید {key} با موفقیت تغییر کرد.")
