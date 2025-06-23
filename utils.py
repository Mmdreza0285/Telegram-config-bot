# utils.py
def format_server(server):
    return f"🌍 کشور: {server.get('country', 'نامشخص')}\n📡 پروتکل: {server.get('protocol', 'نامشخص')}\n🔗 کانفیگ:\n<code>{server.get('config')}</code>"

def get_flag(country):
    flags = {
        "آلمان": "🇩🇪",
        "آمریکا": "🇺🇸",
        "فرانسه": "🇫🇷",
        "هلند": "🇳🇱",
        "ترکیه": "🇹🇷",
        "سوئد": "🇸🇪",
        "سوئیس": "🇨🇭",
    }
    return flags.get(country, "🏳")

