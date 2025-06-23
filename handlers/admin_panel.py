
from aiogram import Router
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import os
from aiogram.filters.callback_data import CallbackData

router = Router()
ADMINS = os.getenv("ADMINS", "").split(",")

class AdminCallback(CallbackData, prefix="admin"):
    action: str

def admin_keyboard():
    kb = InlineKeyboardMarkup(row_width=2)
    kb.add(
        InlineKeyboardButton("📡 مدیریت سرورها", callback_data=AdminCallback(action="manage_servers").pack()),
        InlineKeyboardButton("👥 مدیریت ادمین‌ها", callback_data=AdminCallback(action="manage_admins").pack()),
        InlineKeyboardButton("📊 آمار ربات", callback_data=AdminCallback(action="stats").pack()),
        InlineKeyboardButton("⚙️ ویرایش منو", callback_data=AdminCallback(action="edit_menu").pack()),
    )
    return kb

@router.message(lambda m: str(m.from_user.id) in ADMINS and m.text == "🛠 پنل مدیریت")
async def show_admin_panel(message: Message):
    await message.answer("🔧 به پنل مدیریت خوش آمدید.", reply_markup=admin_keyboard())

@router.callback_query(AdminCallback.filter())
async def admin_callback_handler(callback: CallbackQuery, callback_data: AdminCallback):
    if callback_data.action == "manage_servers":
        await callback.message.answer("📡 بخش مدیریت سرورها (در حال توسعه)")
    elif callback_data.action == "manage_admins":
        await callback.message.answer("👥 بخش مدیریت ادمین‌ها (در حال توسعه)")
    elif callback_data.action == "stats":
        await callback.message.answer("📊 نمایش آمار (در حال توسعه)")
    elif callback_data.action == "edit_menu":
        await callback.message.answer("⚙️ ویرایش منو (در حال توسعه)")
    else:
        await callback.message.answer("❌ گزینه نامعتبر است.")
