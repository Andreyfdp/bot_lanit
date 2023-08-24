from aiogram import Router, types
from aiogram.filters import Command

from utils.base_api import BaseAPI

router = Router()
ip = BaseAPI('https://api.ipify.org/?format=json')
@router.message(Command('my_ip'))
async def answer_ip(message: types.Message):
    await message.reply()


