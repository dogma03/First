from telebot import TeleBot
from telebot import types
import requests

def random_dog():
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']

TOKEN = '7193736397:AAG3icl9y1MeZVnn2_mAIJac5B99vcOqGuY'
bot = TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    dog_btn = types.InlineKeyboardButton(text='Получить собаку', callback_data='123')
    markup.add(dog_btn)

    bot.send_message(message.chat.id, 'салмам по-полам гузмыкбек', reply_markup=markup)
    

@bot.callback_query_handler(func=lambda call: True)
def dog(call):
    if call.data == '123':
        url = random_dog()
        bot.send_message(call.message.chat.id, url)   

@bot.message_handler()
def echo(message):
    bot.send_message(message.chat.id, message.text)


# def callback_handler(call):
#     if call.data == '123':
#             dog(call.message.chat.id)



bot.polling(non_stop=True)