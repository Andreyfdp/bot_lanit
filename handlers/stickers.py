from aiogram import types, Router, F

router = Router()


@router.message(F.sticker)
async def sticker(message: types.Message):
    await message.answer_sticker(message.sticker.file_id)