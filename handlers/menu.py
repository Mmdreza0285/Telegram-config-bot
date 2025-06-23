# handlers/menu.py
from aiogram import Router, F
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from db.mongo import add_user, is_admin

router = Router()

@router.message(F.text == "/start")
async def start_handler(message: Message):
    user_id = message.from_user.id
    username = message.from_user.username or "Unknown"
    await add_user(user_id, username)

    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📡 دریافت سرور رایگان", callback_data="get_servers")],
        [InlineKeyboardButton(text="🤝 دریافت لینک رفرال", callback_data="referral")],
        [InlineKeyboardButton(text="🎁 اهدای کانفیگ", callback_data="donate")],
        [InlineKeyboardButton(text="💬 تماس با پشتیبانی", callback_data="support")],
        [InlineKeyboardButton(text="⚙️ تنظیمات منو", callback_data="menu_edit")],
        [InlineKeyboardButton(text="🔒 خرید اشتراک VIP", callback_data="buy_vip")],
        [InlineKeyboardButton(text="💰 حمایت مالی", callback_data="donate_support")],
    ])

    if await is_admin(user_id):
        kb.inline_keyboard.append([InlineKeyboardButton(text="🛠 پنل مدیریت", callback_data="admin_panel")])

    await message.answer("به ربات خوش آمدید! از منو گزینه مورد نظر را انتخاب کنید:", reply_markup=kb)
