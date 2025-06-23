from aiogram import Router
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters.callback_data import CallbackData

router = Router()

class ProtocolCallback(CallbackData, prefix="proto"):
    protocol: str

class CountryCallback(CallbackData, prefix="country"):
    protocol: str
    country: str

# دیتای نمونه سرورها (شما بعدا می‌تونی از دیتابیس بخونی)
SERVERS = {
    "vmess": {
        "Germany": ["vmess-germany-1", "vmess-germany-2"],
        "USA": ["vmess-usa-1"],
        "France": ["vmess-france-1"],
        "Netherlands": [],
        "Turkey": ["vmess-turkey-1"],
        "Sweden": [],
        "Switzerland": [],
    },
    "vless": {
        "Germany": ["vless-germany-1"],
        "USA": ["vless-usa-1", "vless-usa-2"],
        "France": ["vless-france-1"],
        "Netherlands": ["vless-netherlands-1"],
        "Turkey": [],
        "Sweden": ["vless-sweden-1"],
        "Switzerland": [],
    },
    "ss": {
        "Germany": ["ss-germany-1"],
        "USA": [],
        "France": ["ss-france-1"],
        "Netherlands": [],
        "Turkey": ["ss-turkey-1"],
        "Sweden": [],
        "Switzerland": ["ss-switzerland-1"],
    },
    "outline": {},
    "reality": {},
    "hysteria2": {},
    "warp": {},
}

PROTOCOLS = ["vmess", "vless", "ss", "outline", "reality", "hysteria2", "warp"]
COUNTRIES = ["Germany", "USA", "France", "Netherlands", "Turkey", "Sweden", "Switzerland"]

def make_protocol_keyboard():
    kb = InlineKeyboardMarkup(row_width=2)
    buttons = [InlineKeyboardButton(text=proto.upper(), callback_data=ProtocolCallback(protocol=proto).pack()) for proto in PROTOCOLS]
    kb.add(*buttons)
    return kb

def make_country_keyboard(protocol):
    kb = InlineKeyboardMarkup(row_width=3)
    buttons = []
    for country in COUNTRIES:
        count = len(SERVERS.get(protocol, {}).get(country, []))
        text = f"{country} ({count})"
        buttons.append(InlineKeyboardButton(text=text, callback_data=CountryCallback(protocol=protocol, country=country).pack()))
    kb.add(*buttons)
    return kb

@router.message(lambda m: m.text == "📡 دریافت سرور رایگان")
async def show_protocols(message: Message):
    await message.answer("🌐 پروتکل مورد نظر را انتخاب کنید:", reply_markup=make_protocol_keyboard())

@router.callback_query(ProtocolCallback.filter())
async def show_countries(callback: CallbackQuery, callback_data: ProtocolCallback):
    await callback.message.edit_text(f"🇩🇪 کشور مورد نظر را برای پروتکل <b>{callback_data.protocol.upper()}</b> انتخاب کنید:", reply_markup=make_country_keyboard(callback_data.protocol))

@router.callback_query(CountryCallback.filter())
async def send_servers(callback: CallbackQuery, callback_data: CountryCallback):
    servers = SERVERS.get(callback_data.protocol, {}).get(callback_data.country, [])
    if not servers:
        await callback.message.edit_text("❌ در حال حاضر سروری موجود نیست.")
        return
    text = f"📡 سرورهای <b>{callback_data.protocol.upper()}</b> - {callback_data.country}:\n\n"
    text += "\n".join(f"- {srv}" for srv in servers)
    await callback.message.edit_text(text)
