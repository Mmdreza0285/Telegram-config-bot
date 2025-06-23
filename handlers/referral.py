# handlers/referral.py
from aiogram import Router, F
from aiogram.types import CallbackQuery
from db.mongo import get_user

router = Router()

@router.callback_query(F.data == "referral")
async def referral_handler(callback: CallbackQuery):
    user_id = callback.from_user.id
    user = await get_user(user_id)
    ref_link = f"https://t.me/{callback.bot.username}?start={user_id}"

    await callback.message.answer(f"✅ لینک دعوت شما:\n{ref_link}\nهر کسی از این لینک وارد شود، به آمار دعوت‌های شما افزوده می‌شود.")
    await callback.answer()
