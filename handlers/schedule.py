# handlers/schedule.py
import asyncio
from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from db.mongo import save_schedule_list, get_scheduled_servers

router = Router()

class ScheduleState(StatesGroup):
    waiting_for_servers = State()
    waiting_for_interval = State()
    waiting_for_message = State()
    waiting_for_channel = State()

@router.callback_query(F.data == "schedule")
async def schedule_start(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("🔁 لطفاً لیست سرورها را بفرستید. هر سرور در یک خط.")
    await state.set_state(ScheduleState.waiting_for_servers)
    await callback.answer()

@router.message(ScheduleState.waiting_for_servers)
async def schedule_get_servers(message: Message, state: FSMContext):
    servers = message.text.strip().split("\n")
    await state.update_data(servers=servers)
    await message.answer("⏱ لطفاً فاصله بین هر ارسال (به دقیقه) را وارد کنید:")
    await state.set_state(ScheduleState.waiting_for_interval)

@router.message(ScheduleState.waiting_for_interval)
async def schedule_get_interval(message: Message, state: FSMContext):
    try:
        interval = int(message.text.strip())
        await state.update_data(interval=interval)
        await message.answer("📝 لطفاً متن پیام همراه سرور را وارد کنید:")
        await state.set_state(ScheduleState.waiting_for_message)
    except:
        await message.answer("عدد وارد شده نامعتبر است. دوباره تلاش کنید:")

@router.message(ScheduleState.waiting_for_message)
async def schedule_get_msg(message: Message, state: FSMContext):
    await state.update_data(text=message.text.strip())
    await message.answer("📢 لطفاً @آیدی کانال مقصد را وارد کنید:")
    await state.set_state(ScheduleState.waiting_for_channel)

@router.message(ScheduleState.waiting_for_channel)
async def schedule_save_all(message: Message, state: FSMContext):
    data = await state.get_data()
    servers = data['servers']
    interval = data['interval']
    text = data['text']
    channel = message.text.strip()

    await save_schedule_list(servers, interval, text, channel)
    await message.answer("✅ ارسال زمان‌بندی شده با موفقیت ذخیره شد.")
    await state.clear()

# این تابع باید در جای دیگر پروژه در background اجرا شود:
async def start_scheduler(bot):
    while True:
        schedules = await get_scheduled_servers()
        for sched in schedules:
            if sched['servers']:
                srv = sched['servers'].pop(0)
                await bot.send_message(sched['channel'], f"{sched['text']}\n\n<code>{srv}</code>")
                await save_schedule_list(sched['servers'], sched['interval'], sched['text'], sched['channel'])
        await asyncio.sleep(60)
