# main.py
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from config import BOT_TOKEN
from handlers import (
    menu, server_handler, donate_handler, referral_handler, client_handler,
    account_handler, support_handler, admin_handler, schedule_handler,
    stats_handler, menu_edit_handler
)
from handlers.schedule import start_scheduler

async def main():
    bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher(storage=MemoryStorage())

    dp.include_routers(
        menu.router,
        server_handler.router,
        donate_handler.router,
        referral_handler.router,
        client_handler.router,
        account_handler.router,
        support_handler.router,
        admin_handler.router,
        schedule_handler.router,
        stats_handler.router,
        menu_edit_handler.router,
    )

    asyncio.create_task(start_scheduler(bot))

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
