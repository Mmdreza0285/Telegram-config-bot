# handlers/donate.py
from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from db.mongo import save_donation, get_donations

router = Router()

class DonateState(StatesGroup):
    waiting_for_config = State()

@router.callback_query(F.data == "donate")
async def donate_start(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("📨 لطفاً کانفیگ مورد نظر را بفرستید (بدون تایپ دستی، فقط پیست کنید):")
    await state.set_state(DonateState.waiting_for_config)
    await callback.answer()

@router.message(DonateState.waiting_for_config)
async def donate_receive_config(message: Message, state: FSMContext):
    await save_donation(message.from_user.id, message.text)
    await message.answer("✅ کانفیگ با موفقیت ذخیره شد. سپاس از همکاری شما!")
    await state.clear()

@router.callback_query(F.data == "donate_list")
async def donate_list(callback: CallbackQuery):
    items = await get_donations()
    if not items:
        await callback.message.answer("📭 هیچ سروری اهدا نشده است.")
    else:
        msg = "🎁 سرورهای اهدایی کاربران:\n\n"
        for i, d in enumerate(items):
            msg += f"{i+1}. <code>{d['config']}</code>\n\n"
        await callback.message.answer(msg[:4000])
    await callback.answer()
