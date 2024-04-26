from telebot import TeleBot
from telebot import types
import requests

def random_dog():
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']

TOKEN = '7115888395:AAHdHFe3BOXQi8TdulS3FzY8yieV_TjhPPk'
bot = TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Получить собачку'))
    url = random_dog()
    bot.send_message(message.chat.id, 'Привет, этот бот это пародия на жаба бота')
    bot.send_photo(message.chat.id, url)








bot.polling(non_stop=True)