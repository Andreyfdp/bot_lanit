import asyncio
from aiogram import Bot, Dispatcher
from configuration import settings
from handlers import start, hello, any_text,stickers




async def main():

    bot = Bot(token=settings.TOKEN)

    dp = Dispatcher()
    #dp.include_router(start.router)
    #dp.include_router(stickers.router)
    #dp.include_router(hello.router)
    #dp.include_router(any_text.router)
    dp.include_routers(start.router, stickers.router, hello.router, any_text.router)

    await dp.start_polling(bot)




if __name__ == '__main__':
    asyncio.run(main())