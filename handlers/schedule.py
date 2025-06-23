from aiogram import Router
import os
import asyncio

router = Router()

# اینجا لیست پیام‌های زمان‌بندی شده و کانال‌ها رو نگه می‌داریم
scheduled_messages = []
CHANNELS = os.getenv("CHANNELS", "").split(",")

async def scheduler_loop(bot):
    while True:
        if scheduled_messages and CHANNELS:
            for msg in scheduled_messages:
                for channel in CHANNELS:
                    try:
                        await bot.send_message(chat_id=channel, text=msg)
                    except Exception as e:
                        print(f"خطا در ارسال پیام زمان‌بندی شده به {channel}: {e}")
                await asyncio.sleep(3600)  # هر ۱ ساعت پیام رو ارسال کن
        await asyncio.sleep(60)  # هر دقیقه چک کن

@router.message(lambda m: m.text and m.text.startswith("/schedule "))
async def add_scheduled_message(message):
    if str(message.from_user.id) not in os.getenv("ADMINS", ""):
        await message.answer("❌ شما اجازه استفاده از این دستور را ندارید.")
        return

    text = message.text[10:].strip()
    if not text:
        await message.answer("❌ لطفاً متن پیام برای زمان‌بندی را وارد کنید.")
        return

    scheduled_messages.append(text)
    await message.answer("✅ پیام برای ارسال خودکار هر ۱ ساعت اضافه شد.")
