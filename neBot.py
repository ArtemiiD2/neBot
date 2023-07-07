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

#C:\Users\Algoritmika\Desktop\коллажик\банч.jpg

@bot.message_handler(content_types=['text'])
async def send_ffile(message):
    chat_id = message.from_user.id
    path_ffile = message.text
    try:
        await bot.send_document(chat_id, open(path_ffile,'rb'))
    except:
        await bot.send_message(chat_id,'Такого файла нет.')

# @bot.message_handler(commands=['random'])
# async def random(message):
#     chat_id = message.from_user.id
#     bot_message = await bot.send_dice(chat_id, '🎲')
#     print(bot_message.dice.value)
#
# @bot.message_handler(commands=['contact'])
# async def contact(message):
#     chat_id = message.from_user.id
#     await bot.send_message(chat_id, '<a href="tg://user?id=5794033915">my account</a>')
#
# @bot.message_handler(commands=['allfiles'])
# async def allfiles(message):
#     chat_id = message.from_user.id
#     await bot.send_message(chat_id, files)




import asyncio
asyncio.run(bot.polling())