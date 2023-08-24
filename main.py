import asyncio
import logging
from aiogram import Bot, Dispatcher
from configuration import settings
from handlers import start, hello, any_text,stickers, photo, cat, weather
from utils.commands import defaunt_commands

logging.basicConfig(level=logging.INFO)

bot = Bot(token=settings.TOKEN)
dp = Dispatcher()
dp.include_routers(start.router,cat.router,weather.router, stickers.router, hello.router, any_text.router, photo.router)
async def main():
    await defaunt_commands(bot)
    await dp.start_polling(bot)




if __name__ == '__main__':
    asyncio.run(main())