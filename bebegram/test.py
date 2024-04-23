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
    # markup = types.InlineKeyboardMarkup()
    # dog_btn = types.InlineKeyboardButton('Получить собаку')
    # markup.add(dog_btn)

    bot.send_message(message.chat.id, 'салмам по-полам гузмыкбек') #reply_markup=markup)
    
@bot.message_handler(commands=['dog'])
def dog(message):
    url = random_dog()
    bot.send_message(message.chat.id, url)

@bot.message_handler()
def echo(message):
    bot.send_message(message.chat.id, message.text)





bot.polling(non_stop=True)