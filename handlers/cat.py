from aiogram import Router, types
from aiogram.filters import Command

from utils.base_api import BaseAPI

router = Router()
cat_api = BaseAPI('https://cataas.com')
@router.message(Command('cat'))
async def get_cat_pickture(message: types.Message):
    cat_pick = await cat_api.get_data('/cat')
    await message.reply_photo(types.BufferedInputFile(cat_pick, 'cat.png'))
