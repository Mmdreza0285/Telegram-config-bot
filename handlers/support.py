# handlers/support.py
from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from db.mongo import get_admins

router = Router()

class SupportState(StatesGroup):
    waiting_for_message = State()

@router.callback_query(F.data == "support")
async def start_support(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("لطفاً پیام خود را بنویسید، پشتیبانی به شما پاسخ خواهد داد.")
    await state.set_state(SupportState.waiting_for_message)
    await callback.answer()

@router.message(SupportState.waiting_for_message)
async def receive_support_message(message: Message, state: FSMContext):
    admins = await get_admins()
    for admin_id in admins:
        await message.bot.send_message(admin_id, f"📨 پیام پشتیبانی جدید از کاربر @{message.from_user.username} ({message.from_user.id}):\n{message.text}")
    await message.answer("✅ پیام شما ارسال شد. پشتیبانی بزودی پاسخ خواهد داد.")
    await state.clear()
