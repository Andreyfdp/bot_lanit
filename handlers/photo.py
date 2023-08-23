from aiogram import Router, types,F

router = Router()
@router.message(F.photo)
async def process_photo(message: types.Message):
    await message.answer_photo(message.photo[0].file_id)
