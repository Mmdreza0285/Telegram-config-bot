from aiogram import Router
from aiogram.types import Message, ContentType
from aiogram.filters import Command

router = Router()

# فرضا سرورهای اهدایی در دیتابیس ذخیره می‌شود
donated_servers = []

@router.message(lambda m: m.text == "📬 اهدا سرور")
async def donate_prompt(message: Message):
    await message.answer("📩 لطفاً کانفیگ خود را به صورت فایل یا متن ارسال کنید.")

@router.message(content_types=[ContentType.TEXT, ContentType.DOCUMENT, ContentType.PHOTO])
async def receive_donate(message: Message):
    # فقط اگر قبلا درخواست اهدا داده باشد، ذخیره نشود (به عنوان مثال)
    if message.text or message.document:
        # ساده ذخیره‌سازی در لیست موقتی
        donated_servers.append({
            "user_id": message.from_user.id,
            "content": message.text if message.text else "<فایل یا عکس ارسال شده>",
        })
        await message.answer("✅ کانفیگ شما دریافت شد و پس از بررسی منتشر خواهد شد.\nمتشکریم از همکاری شما!")

