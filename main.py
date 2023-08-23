import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from configuration import settings

bot_token = settings.TOKEN
bot = Bot(token= bot_token)

#asyncio.run( bot.send_message(1156167454, 'hi'))

dp = Dispatcher()
async def main():
    await dp.start_polling(bot)


@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")



if __name__ == '__main__':
    asyncio.run(main())