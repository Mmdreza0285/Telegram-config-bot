from aiogram import Router
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.filters.callback_data import CallbackData
import os

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
        InlineKeyboardButton("🗑️ حذف سرورها", callback_data=AdminCallback(action="delete_servers").pack()),
    )
    return kb

@router.message(lambda m: str(m.from_user.id) in ADMINS and m.text == "🛠 پنل مدیریت")
async def show_admin_panel(message: Message):
    await message.answer("🔧 به پنل مدیریت خوش آمدید.", reply_markup=admin_keyboard())

@router.callback_query(AdminCallback.filter())
async def admin_callback_handler(callback: CallbackQuery, callback_data: AdminCallback):
    if callback_data.action == "manage_servers":
        await callback.message.answer("📡 بخش مدیریت سرورها در دست توسعه است.")
    elif callback_data.action == "manage_admins":
        await callback.message.answer("👥 بخش مدیریت ادمین‌ها در دست توسعه است.")
    elif callback_data.action == "stats":
        await callback.message.answer("📊 بخش آمار در دست توسعه است.")
    elif callback_data.action == "edit_menu":
        await callback.message.answer("⚙️ بخش ویرایش منو در دست توسعه است.")
    elif callback_data.action == "delete_servers":
        await callback.message.answer("🗑️ بخش حذف سرورها در دست توسعه است.")
    else:
        await callback.message.answer("❌ گزینه نامعتبر است.")
