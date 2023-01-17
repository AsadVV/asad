import logging
import telebot
import parse
from aiogram import Bot, Dispatcher, executor, types
logging.basicConfig(level=logging.INFO)
bot = telebot.TeleBot('5897249172:AAEgHJFb8mDsaUognG39eTkmvbOMPggtHBs')








@bot.message_handler(commands=['new'])
def new(message):
    bot.send_message(message.chat.id, parse.asad())

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет,{message.from_user.first_name}'
    bot.send_message(message.chat.id, mess)
    
@bot.message_handler()
def user_get(message):
    if message.text == "Hello":
       bot.send_message(message.chat.id, 'И тебе привет')
    elif message.text == "ID":
        bot.send_message(message.chat.id, f'Вот твой ID: {message}')

    else:
        bot.send_message(message.chat.id, 'Пишите нормально')






bot.polling(none_stop=True)




