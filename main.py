
import asyncio
import os
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from handlers import configs, donate, referral, support, admin_panel, schedule, stats, menu_edit

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# ثبت همه روترها
dp.include_router(configs.router)
dp.include_router(donate.router)
dp.include_router(referral.router)
dp.include_router(support.router)
dp.include_router(admin_panel.router)
dp.include_router(schedule.router)
dp.include_router(stats.router)
dp.include_router(menu_edit.router)

async def main():
    asyncio.create_task(schedule.scheduler_loop(bot))
    print("ربات شروع به کار کرد...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
