from aiogram import Dispatcher, types
from aiogram.types import Message

from keyboards import main_menu

async def handle_menu_selection(message: Message):
    text = message.text

    if text == "📡 دریافت سرور رایگان":
        await message.answer("🌍 لطفاً پروتکل موردنظر را انتخاب کنید:", reply_markup=main_menu("protocols"))
    
    elif text == "🎁 اهدای سرور":
        await message.answer("لطفاً فایل یا متن کانفیگ خود را ارسال کنید.\nما بررسی و منتشر خواهیم کرد.")

    elif text == "👥 رفرال من":
        ref_link = f"https://t.me/{(await message.bot.get_me()).username}?start={message.from_user.id}"
        await message.answer(f"📨 لینک دعوت شما:\n{ref_link}")

    elif text == "🔧 پنل مدیریت":
        await message.answer("🔐 ورود به پنل مدیریت فعال نیست. در حال توسعه است.")

    elif text == "🧩 لیست کلاینت‌ها":
        await message.answer("📲 لیست کلاینت‌ها به‌زودی بارگذاری می‌شود.")

    elif text == "📊 وضعیت اکانت":
        await message.answer("📌 اطلاعات اکانت شما:\n(در حال توسعه)")

    elif text == "📬 ارتباط با پشتیبانی":
        await message.answer("💬 لطفاً پیام خود را بنویسید، ما بررسی می‌کنیم.")

    elif text == "📤 ارسال نظر":
        await message.answer("📝 لطفاً نظرتان را ارسال کنید، ناشناس دریافت خواهد شد.")

    elif text == "💸 حمایت مالی":
        await message.answer("💳 این بخش بزودی فعال خواهد شد.")

    elif text == "🌟 خرید اشتراک VIP":
        await message.answer("🚀 بخش VIP به‌زودی فعال می‌شود.")

    else:
        await message.answer("❌ گزینه نامعتبر است.", reply_markup=main_menu())

def register_menu_handlers(dp: Dispatcher, db):
    dp.register_message_handler(handle_menu_selection)
