from telebot.async_telebot import AsyncTeleBot
from telebot.types import ReplyKeyboardMarkup, InlineKeyboardMarkup
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())
TOKEN = os.getenv('TOKEN')

bot = AsyncTeleBot(TOKEN, parse_mode='HTML')

@bot.message_handler(commands=['start'])
async def send_welcome(message):
    chat_id = message.from_user.id
    await bot.send_message(chat_id, 'Привет, я неБот')
    print(message)

@bot.message_handler(commands=['random'])
async def random(message):
    chat_id = message.from_user.id
    bot_message = await bot.send_dice(chat_id, '🎲')
    print(bot_message.dice.value)

@bot.message_handler(commands=['contact'])
async def contact(message):
    chat_id = message.from_user.id
    await bot.send_message(chat_id, '<a href="tg://user?id=5794033915">my account</a>')

@bot.message_handler(commands=['timer'])
async def timer(message):
    chat_id = message.from_user.id
    await bot.send_message(chat_id, 'На сколько?  (сек)')
    time = chat_id
    bot_message = await bot.send_message(chat_id, 'Таймер начался -', time, 'секунд')
    for i in range(1, time):
        await asyncio.sleep(1)
        await bot.edit_message_text(f'{time - i} секуунд прошло', chat_id, bot_message.id)
    await bot.delete_message(chat_id, bot_message.id)





















































































import asyncio
asyncio.run(bot.polling())