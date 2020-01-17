""" Итак, для начала определим логику бота, то, как он будет выглядеть. Во-первых, надо обязательно отвечать на
команду /start. Во-вторых, надо каким-то образом присылать пользователю картинку с котиком, а перед этим эту картинку
надо откуда-то взять """
import telebot
import requests
from telebot import apihelper
# Этот типа нужен для создания реплай-клавиатур
from telebot.types import ReplyKeyboardMarkup

# для обхода блокировки
apihelper.proxy = {'https': 'https://85.132.71.82:3128'}
# токен бота
TOKEN = '1029144706:AAEtnPyANF0u4dIHoc5v-lx_MyrTODU3sgI'
bot = telebot.TeleBot(TOKEN)
# ссылка с котиками
url = 'https://api.thecatapi.com/v1/images/search?mime_type=jpg'


@bot.message_handler(commands=['start'])
def start(message):
    markup = ReplyKeyboardMarkup(True, False)
    # кнопка
    markup.row('Получить котика!')
    # отправка сообщения
    bot.send_message(message.from_user.id, 'Привет, нажми кнопку ниже', reply_markup=markup)


@bot.message_handler(regexp='Получить котика!')
def cats(message):
    response = requests.get(url)
    data = response.json()
    cat = data[0]['url']
    bot.send_photo(message.from_user.id, cat)


bot.polling(none_stop=True)
