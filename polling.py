import asyncio
import logging
import os

from dotenv import load_dotenv
from maxapi import Bot, Dispatcher
from maxapi.enums.parse_mode import ParseMode
from maxapi.types import BotStarted, Command, MessageCreated

logging.basicConfig(level=logging.INFO)

load_dotenv()
bot = Bot(os.environ['ACCESS_TOKEN'])
dp = Dispatcher()

CHAT_ID = -73444661955086
STATUS_MESSAGE = "Статус: онлайн"
STATUS_INTERVAL = 60  # 30 минут в секундах

# Ответ бота при нажатии на кнопку "Начать"
@dp.bot_started()
async def bot_started(event: BotStarted):
    await event.bot.send_message(
        chat_id=event.chat_id,
        text='Привет! Отправь мне /start'
    )

# Ответ бота на команду /start
@dp.message_created(Command('start'))
async def hello(event: MessageCreated):
    await event.message.answer(f"Пример чат-бота для MAX 💙")


async def send_status_updates(bot_instance):
    """Периодическая отправка статуса в чат каждые 30 минут"""
    while True:
        try:
            await bot_instance.send_message(
                chat_id=CHAT_ID,
                text=STATUS_MESSAGE
            )
            logging.info(f"Отправлен статус в чат {CHAT_ID}")
        except Exception as e:
            logging.error(f"Ошибка при отправке статуса: {e}")
        await asyncio.sleep(STATUS_INTERVAL)


async def main():
    # Запускаем периодическую отправку статуса
    # asyncio.create_task(send_status_updates(bot))
    # Запускаем polling
    bot_name = await bot.get_me()
    await bot.send_message(CHAT_ID, text=f"Бот **{bot_name.first_name}** запущен.", parse_mode=ParseMode.MARKDOWN)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())