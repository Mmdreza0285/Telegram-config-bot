# handlers/admin_panel.py
from aiogram import Router, F
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from db.mongo import get_user_count, is_admin

router = Router()

@router.callback_query(F.data == "admin_panel")
async def admin_panel_handler(callback: CallbackQuery):
    user_id = callback.from_user.id
    if not await is_admin(user_id):
        await callback.answer("شما ادمین نیستید.", show_alert=True)
        return

    user_count = await get_user_count()
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="➕ افزودن ادمین", callback_data="add_admin")],
        [InlineKeyboardButton(text="📊 آمار ربات", callback_data="stats")],
        [InlineKeyboardButton(text="📤 پیام همگانی", callback_data="broadcast")],
        [InlineKeyboardButton(text="🕐 زمان‌بندی ارسال", callback_data="schedule")],
        [InlineKeyboardButton(text="📝 ویرایش منو", callback_data="menu_edit")]
    ])
    await callback.message.answer(f"به پنل مدیریت خوش آمدید. کاربران فعلی: {user_count}", reply_markup=kb)
    await callback.answer()
