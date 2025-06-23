
from aiogram import Router
from aiogram.types import Message
import os
import asyncio

router = Router()

scheduled_messages = []

@router.message(lambda m: m.text and m.text.startswith("/schedule "))
async def add_scheduled_message(message: Message):
    text = message.text[10:].strip()
    if not text:
        await message.answer("❌ لطفاً متن پیام برای زمان‌بندی
