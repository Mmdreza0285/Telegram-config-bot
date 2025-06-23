from aiogram import Router
from aiogram.types import Message

router = Router()

@router.message(lambda m: m.text == "🎁 لینک رفرال")
async def referral_link(message: Message):
    user_id = message.from_user.id
    username = message.bot.username
    link = f"https://t.me/{username}?start={user_id}"
    await message.answer(f"🔗 لینک دعوت شما:\n{link}")

