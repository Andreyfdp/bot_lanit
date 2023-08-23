import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from configuration import settings
import handlers


bot_token = settings.TOKEN
bot = Bot(token= bot_token)

#asyncio.run( bot.send_message(1156167454, 'hi'))

dp = Dispatcher()
async def main():
    from handlers import dp
    await dp.start_polling(bot)








if __name__ == '__main__':
    asyncio.run(main())