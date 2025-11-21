#импорт библиотек
import logging

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters.command import Command
import os

# инициализация объектов

# bot = Bot(token='ТУТ БЫЛ ТОКЕН')
TOKEN = os.getenv('TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher()
logging.basicConfig(level=logging.INFO)

# Словарь букв по приказу МИД

trans = {'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 
    'Ё': 'E', 'Ж': 'ZH', 'З': 'Z', 'И': 'I', 'Й': 'I', 'К': 'K', 'Л': 'L',
    'М': 'M', 'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T',
    'У': 'U', 'Ф': 'F', 'Х': 'KH', 'Ц': 'TS', 'Ч': 'CH', 'Ш': 'SH', 
    'Щ': 'SHCH', 'Ъ': 'IE', 'Ы': 'Y', 'Ь': '', 'Э': 'E', 'Ю': 'IU', 'Я': 'IA'}

#Функция перевода имени, заменяем каждую букву по словарю

def transliterate_name(name):
    transliterated = ''
    for letter in name:
        if letter in trans:
            transliterated += trans[letter]
        else:
            transliterated += letter
    return  transliterated.title()

# обработка команды start

@dp.message(Command(commands=['start']))
async def proccess_command_start(message: Message):
    user_name = message.from_user.full_name.upper()
    user_id = message.from_user.id
    user_name = transliterate_name(user_name)
    text = f'Привет, {user_name}!'
    logging.info(f'{user_name} {user_id} запустил бота')
    await bot.send_message(chat_id=user_id, text=text)

# Обработка всех сообщений

@dp.message()
async def send_echo(message: Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = message.text
    logging.info(f'{user_name} {user_id}: {text}')
    await message.answer(transliterate_name(text.upper()))

# Запуск процесса пуллинга

if __name__ == '__main__':
    dp.run_polling(bot)