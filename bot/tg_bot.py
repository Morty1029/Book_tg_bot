import asyncio
import logging
import requests

from bot.config import Config
from BookStates import BookStates

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.fsm.context import FSMContext



CONFIG = Config()
DISPATCHER = Dispatcher()
BOT = Bot(token=CONFIG.tg_token)
logging.basicConfig(level=logging.INFO)

books = {
    "Гарри Поттер и Философский камень": 1,
    "Гарри Поттер и Тайная комната": 2,
    "Гарри Поттер и Узник Азкабана": 3,
    "Гарри Поттер и Кубок огня": 4,
    "Гарри Поттер и Орден Феникса": 5,
    "Гарри Поттер и Принц Полукровка": 6,
    "Гарри Поттер и Дары смерти": 7,
}

# Создаем кнопки для меню
menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📖 Задать вопрос по книге")],
    ],
    resize_keyboard=True
)

# Кнопки с выбором книг
books_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Гарри Поттер и Философский камень")],
        [KeyboardButton(text="Гарри Поттер и Тайная комната")],
        [KeyboardButton(text="Гарри Поттер и Узник Азкабана")],
        [KeyboardButton(text="Гарри Поттер и Кубок огня")],
        [KeyboardButton(text="Гарри Поттер и Орден Феникса")],
        [KeyboardButton(text="Гарри Поттер и Принц Полукровка")],
        [KeyboardButton(text="Гарри Поттер и Дары смерти")],
    ],
    resize_keyboard=True
)


@DISPATCHER.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        text="Привет! Я - бот, который в любой момент может подсказать содержание одной из книг, о которых я знаю",
        reply_markup=menu_keyboard
    )

"""
@DISPATCHER.message()
async def echo(message: types.Message):
    await message.answer(f'Вы написали: {message.text}')
"""

@DISPATCHER.message(F.text == "📖 Задать вопрос по книге")
async def ask_series(message: types.Message,  state: FSMContext):
    await message.answer(
        text="По какой из книг ты хотел бы задать свой вопрос?",
        reply_markup=books_keyboard
    )
    await state.set_state(BookStates.series)
    await state.update_data(series='GP')


@DISPATCHER.message(F.text, BookStates.series)
async def ask_book(message: types.Message, state: FSMContext):
    await state.set_state(BookStates.book_name)
    await state.update_data(book_name=message.text)
    await message.answer(
        text=f"Я буду рад ответить на любой твой вопрос по книге {message.text}"
    )

@DISPATCHER.message(F.text, BookStates.book_name)
async def answer_book_question(message: types.Message, state: FSMContext):
    data = await state.get_data()
    book_num = books[data.get('book_name')]
    answer = await get_answer(message.text, book_num=book_num)
    await message.answer(
        text=f"{answer}"
    )



async def get_answer(prompt, book_num=None):
    response = requests.get(f'{CONFIG.host}:{CONFIG.port}/get_answer', params={'prompt': prompt, 'book_num': book_num})
    return response.json()['answer']

async def main():
    await DISPATCHER.start_polling(BOT)




if __name__ == "__main__":
    asyncio.run(main())
