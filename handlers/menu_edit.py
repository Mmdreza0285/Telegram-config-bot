# handlers/menu_edit.py
from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from db.mongo import save_menu_texts, get_menu_texts

router = Router()

class MenuEditState(StatesGroup):
    waiting_for_texts = State()

@router.callback_query(F.data == "menu_edit")
async def start_edit(callback: CallbackQuery, state: FSMContext):
    texts = await get_menu_texts()
    msg = "📝 متن فعلی منو:\n"
    for k, v in texts.items():
        msg += f"{k}: {v}\n"
    msg += "\nپیام جدید را به صورت:\nkey=value در هر خط بفرستید"
    await callback.message.answer(msg)
    await state.set_state(MenuEditState.waiting_for_texts)
    await callback.answer()

@router.message(MenuEditState.waiting_for_texts)
async def save_texts(message: Message, state: FSMContext):
    lines = message.text.split("\n")
    updated = {}
    for line in lines:
        if '=' in line:
            k, v = line.split('=', 1)
            updated[k.strip()] = v.strip()
    await save_menu_texts(updated)
    await message.answer("✅ منو با موفقیت ویرایش شد.")
    await state.clear()
