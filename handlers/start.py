from aiogram import types
from aiogram.filters import Command
from main import dp


@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")