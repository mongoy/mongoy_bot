import telebot
from telebot import apihelper
from telebot import types


# для обхода блокировки
apihelper.proxy = {'https': 'https://85.132.71.82:3128'}
# токен бота
TOKEN = '1029144706:AAEtnPyANF0u4dIHoc5v-lx_MyrTODU3sgI'
bot = telebot.TeleBot(TOKEN)

# спросит имя фамилию и сколько лет
name = ''
surname = ''
age = 0


# объявим метод для получения текстовых сообщений
@bot.message_handler(content_types=['text'])
def start(message):
    # if message == '/reg':
    bot.send_message(message.from_user.id, 'Как тебя зовут?')
    bot.register_next_step_handler(message, get_name)
    # else:
    #    bot.send_message(message.from_user.id, 'Напиши /reg')


def get_name(message):  # Получим фамилию
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Какая у тебя фамилия?')
    bot.register_next_step_handler(message, get_surname)


def get_surname(message):
    global surname
    surname = message.text
    bot.send_message('Сколько тебе лет?')
    bot.register_next_step_handler(message, get_age)


# def get_age(message):
#     global age
#     while age == 0:  # проверяем что возраст изменился
#         try:
#             age = int(message.text)  # проверяем, что возраст введен корректно
#         except Exception:
#             bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')
#     bot.send_message(message.from_user.id, 'Тебе ' + str(age) + ' лет, тебя зовут ' + name + ' ' + surname + '?')


# def hello(message):
#     bot.send_message(message.from_user.id, 'Привет, {name}. Рад тебя видеть!'.format(name=message.text))

def get_age(message):
    global age
    while age == 0:  # проверяем что возраст изменился
        try:
             age = int(message.text)  # проверяем, что возраст введен корректно
        except Exception:
            bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')
            keyboard = types.InlineKeyboardMarkup()  # наша клавиатура
            key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')  # кнопка «Да»
            keyboard.add(key_yes)  # добавляем кнопку в клавиатуру
            key_no= types.InlineKeyboardButton(text='Нет', callback_data='no')
            keyboard.add(key_no)
            question = 'Тебе '+str(age)+' лет, тебя зовут '+name+' '+surname+'?'
            bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "yes":  # call.data это callback_data, которую мы указали при объявлении кнопки
        # код сохранения данных, или их обработки
        bot.send_message(call.message.chat.id, 'Запомню : )')
    elif call.data == "no":
        # переспрашиваем
        pass


bot.polling(none_stop=True, interval=0)
