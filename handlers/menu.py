# handlers/menu.py
from aiogram import Router
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from db.mongo import get_menu_texts

router = Router()

@router.message()
async def main_menu(message: Message):
    texts = await get_menu_texts()
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=texts.get("get_servers", "📡 دریافت سرور رایگان"), callback_data="get_servers")],
        [InlineKeyboardButton(text=texts.get("donate", "🎁 اهدای سرور"), callback_data="donate")],
        [InlineKeyboardButton(text=texts.get("referral", "👥 رفرال"), callback_data="referral")],
        [InlineKeyboardButton(text=texts.get("clients", "💻 لیست کلاینت‌ها"), callback_data="clients")],
        [InlineKeyboardButton(text=texts.get("account_status", "📇 وضعیت حساب"), callback_data="account_status")],
        [InlineKeyboardButton(text=texts.get("support", "📩 تماس با پشتیبانی"), callback_data="support")],
        [InlineKeyboardButton(text=texts.get("vip", "💎 خرید اشتراک VIP"), callback_data="vip")],
        [InlineKeyboardButton(text=texts.get("donate_money", "💰 حمایت مالی"), callback_data="donate_money")],
        [InlineKeyboardButton(text=texts.get("admin_panel", "🛠 پنل مدیریت"), callback_data="admin_panel")]
    ])
    await message.answer(texts.get("welcome", "به ربات خوش آمدید. از منوی زیر انتخاب کنید:"), reply_markup=keyboard)
