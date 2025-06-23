
from aiogram import Router
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters.callback_data import CallbackData

router = Router()

class ProtocolCallback(CallbackData, prefix="proto"):
    protocol: str

class CountryCallback(CallbackData, prefix="country"):
    protocol: str
    country: str

# نمونه داده سرورها (در عمل باید از دیتابیس خوانده شود)
SERVERS = {
    "vmess": {
        "Germany": ["vmess-server1-germany", "vmess-server2-germany"],
        "USA": ["vmess-server1-usa"],
        "France": [],
        "Turkey": ["vmess-server1-turkey"],
        "Sweden": [],
        "Switzerland": [],
        "Netherlands": [],
    },
    "vless": {
        "Germany": ["vless-server1-germany"],
        "USA": ["vless-server1-usa", "vless-server2-usa"],
        "France": ["vless-server1-france"],
        "Turkey": [],
        "Sweden": ["vless-server1-sweden"],
        "Switzerland": [],
        "Netherlands": ["vless-server1-netherlands"],
    },
    "ss": {
        "Germany": ["ss-server1-germany"],
        "USA": [],
        "France": ["ss-server1-france"],
        "Turkey": ["ss-server1-turkey"],
        "Sweden": [],
        "Switzerland": ["ss-server1-switzerland"],
        "Netherlands": [],
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
        servers = SERVERS.get(protocol, {}).get(country, [])
        count = len(servers)
        text = f"{country} ({count})" if count > 0 else f"{country} (0)"
        buttons.append(InlineKeyboardButton(text=text, callback_data=CountryCallback(protocol=protocol, country=country).pack()))
    kb.add(*buttons)
    return kb

@router.message(lambda m: m.text == "📡 دریافت سرور رایگان")
async def protocol_menu(message: Message):
    await message.answer("🌐 پروتکل مورد نظر را انتخاب کنید:", reply_markup=make_protocol_keyboard())

@router.callback_query(ProtocolCallback.filter())
async def country_menu(callback: CallbackQuery, callback_data: ProtocolCallback):
    await callback.message.edit_text(f"🇩🇪 کشور مورد نظر را برای پروتکل <b>{callback_data.protocol.upper()}</b> انتخاب کنید:", reply_markup=make_country_keyboard(callback_data.protocol))

@router.callback_query(CountryCallback.filter())
async def send_servers(callback: CallbackQuery, callback_data: CountryCallback):
    servers = SERVERS.get(callback_data.protocol, {}).get(callback_data.country, [])
    if not servers:
        await callback.message.edit_text("❌ در حال حاضر سروری در این دسته بندی موجود نیست.")
        return
    text = f"📡 سرورهای <b>{callback_data.protocol.upper()}</b> - {callback_data.country}:\n"
    text += "\n".join(f"- {srv}" for srv in servers)
    await callback.message.edit_text(text)
