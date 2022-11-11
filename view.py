from aiogram import types
from create_bot import bot


async def hello(message: types.Message):
    await bot.send_message(message.from_user.id, f'{message.from_user.first_name}, привет!'
                                                 f'Сегодня будем делить конфеты')