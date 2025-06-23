# handlers/free_servers.py
from aiogram import Router, F
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from db.mongo import get_servers

router = Router()

protocols = ["VLESS", "VMESS", "SS", "Outline", "Reality", "Hysteria2", "Warp"]
countries = [
    ("🇩🇪 آلمان", "Germany"),
    ("🇺🇸 آمریکا", "USA"),
    ("🇫🇷 فرانسه", "France"),
    ("🇳🇱 هلند", "Netherlands"),
    ("🇹🇷 ترکیه", "Turkey"),
    ("🇸🇪 سوئد", "Sweden"),
    ("🇨🇭 سوئیس", "Switzerland")
]

@router.callback_query(F.data == "get_servers")
async def choose_protocol(callback: CallbackQuery):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=protocol, callback_data=f"protocol_{protocol}")] for protocol in protocols
    ])
    await callback.message.answer("لطفاً پروتکل مورد نظر را انتخاب کنید:", reply_markup=kb)
    await callback.answer()

@router.callback_query(F.data.startswith("protocol_"))
async def choose_country(callback: CallbackQuery):
    protocol = callback.data.split("_")[1]
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=flag, callback_data=f"servers_{protocol}_{country}")] for flag, country in countries
    ])
    await callback.message.answer(f"پروتکل {protocol} انتخاب شد. حالا کشور را انتخاب کنید:", reply_markup=kb)
    await callback.answer()

@router.callback_query(F.data.startswith("servers_"))
async def show_servers(callback: CallbackQuery):
    _, protocol, country = callback.data.split("_")
    servers = await get_servers(protocol=protocol, country=country)
    if not servers:
        await callback.message.answer("❌ هیچ سروری برای این دسته‌بندی موجود نیست.")
    else:
        msg = f"✅ لیست سرورهای {protocol} در کشور {country}:\n"
        for s in servers:
            msg += f"\n<code>{s.get('server')}</code>"
        await callback.message.answer(msg)
    await callback.answer()
