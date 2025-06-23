from aiogram import Router
from aiogram.types import Message, ContentType

router = Router()

donated_servers = []

@router.message(lambda m: m.text == "📬 اهدا سرور")
async def prompt_donate(message: Message):
    await message.answer("📩 کانفیگ سرور خود را ارسال کنید (متن یا فایل).")

@router.message(content_types=[ContentType.TEXT, ContentType.DOCUMENT])
async def receive_donation(message: Message):
    content = ""
    if message.text:
        content = message.text
    elif message.document:
        content = f"<فایل: {message.document.file_name}>"
    donated_servers.append({
        "user_id": message.from_user.id,
        "content": content,
    })
    await message.answer("✅ کانفیگ شما دریافت شد و پس از بررسی منتشر می‌شود. متشکریم!")
