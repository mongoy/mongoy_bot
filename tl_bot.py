import telebot
from telebot import apihelper


# для обхода блокировки
apihelper.proxy = {'https': 'https://85.132.71.82:3128'}
# токен бота
TOKEN = '1029144706:AAEtnPyANF0u4dIHoc5v-lx_MyrTODU3sgI'
bot = telebot.TeleBot(TOKEN)


# объявим метод для получения текстовых сообщений
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


bot.polling(none_stop=True, interval=0)
