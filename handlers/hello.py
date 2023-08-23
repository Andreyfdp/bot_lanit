from aiogram import types, Router, F

router = Router()


@router.message(F.text.lower() == 'привет')
async def answer_to_any_text(message: types.Message):
    await message.answer(f'Привет, {message.from_user.full_name}!!!')