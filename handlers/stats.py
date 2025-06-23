# handlers/stats.py
from aiogram import Router, F
from aiogram.types import CallbackQuery
from db.mongo import get_user_count, get_server_count

router = Router()

@router.callback_query(F.data == "stats")
async def stats_handler(callback: CallbackQuery):
    users = await get_user_count()
    servers = await get_server_count()
    msg = f"📊 آمار کلی ربات:\n\n👤 کاربران: {users}\n📦 سرورها: {servers}"
    await callback.message.answer(msg)
    await callback.answer()
