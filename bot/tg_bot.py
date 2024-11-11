import asyncio
import logging

from bot.config import Config
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command

CONFIG = Config()
DISPATCHER = Dispatcher()
BOT = Bot(token=CONFIG.tg_token)
logging.basicConfig(level=logging.INFO)


@DISPATCHER.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        text="Привет! Я - бот, который в любой момент может подсказать содержание одной из книг, о которых я знаю"
    )


@DISPATCHER.message(F.text)
async def echo(message: types.Message):
    await message.answer(text=message.text)


async def main():
    await DISPATCHER.start_polling(BOT)


if __name__ == "__main__":
    asyncio.run(main())
