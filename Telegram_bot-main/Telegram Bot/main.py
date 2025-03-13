import asyncio
from aiogram import Bot, Dispatcher

from app.handlers import router
from dotenv import load_dotenv
import os


async def main():
    load_dotenv()  # Загружаем переменные окружения из .env файла
    bot = Bot(os.getenv('TOKEN'))  # Создаем экземпляр класса Bot, используя токен из переменной окружения
    dp = Dispatcher()  # Создаем диспетчер для маршрутизации сообщений
    dp.include_router(router)  # Добавляем роутер с обработчиками сообщений
    await dp.start_polling(bot)  # Запускаем бесконечный цикл опроса обновлений от API Telegram

if __name__ == '__main__':
    try:
        asyncio.run(main())  # Запускаем функцию main в асинхронном режиме
    except KeyboardInterrupt:
        print('Бот выключен')
