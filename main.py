import telebot
from telebot import types
global str
import sqlite3

otv = ""
login = ""
pas = ""




login=str(login)
pas=str(pas)

bot = telebot.TeleBot('782395944:AAEu8XayCTB-LbM-jbSCIe8fpcvXSSfq8bM')


@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    regbtn = types.KeyboardButton('Регистрация')
    logbtn = types.KeyboardButton('Вход')
    markup.row(logbtn, regbtn)
    bot.send_message(message.chat.id, "Рад тебя приветствовать мой друг", reply_markup=markup)


@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, 'https://pypi.org/project/pyTelegramBotAPI/#bots-using-this-api')
    bot.send_message(message.chat.id, "==============================================================")
    bot.send_message(message.chat.id, 'https://habr.com/ru/post/442800/')
    bot.send_message(message.chat.id, "==============================================================")
    bot.send_message(message.chat.id, 'https://habr.com/ru/post/448310/')
    bot.send_message(message.chat.id, "==============================================================")
    bot.send_message(message.chat.id, "https://python-scripts.com/sqlite")


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'привет':
        bot.send_message(message.chat.id, 'Привет, мой создатель')
    if message.text == 'тест':
        bot.send_message(message.chat.id, str(message.text()))
    elif message.text == 'пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')

    # вход
    if message.text == 'Вход':
        hide_keyboard = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, 'Введи логин',reply_markup=hide_keyboard)
        bot.register_next_step_handler(message, get_login)

        
    if message.chat.id == 480718174:
        if message.text == 'Мне грустно':
            bot.send_message(message.chat.id, "Не обижайся сладкая булочка,ты лучший")
    print(message.chat.id, message.text)



def get_login(message):
    global login
    login=message.text
    hide_keyboard = types.ReplyKeyboardRemove()
    bot.send_message(message.from_user.id,"Какой пароль?",reply_markup=hide_keyboard)
    bot.register_next_step_handler(message,get_pas)

def get_pas(message):
    global pas
    pas=message.text
    bot.send_message(message.from_user.id,"Твой логин " + login)
    bot.send_message(message.from_user.id, "Твой пароль " + pas)


    markup = types.InlineKeyboardMarkup(row_width=1)
    yes_btn = types.InlineKeyboardButton(text='Да',callback_data="Да")
    no_btn = types.InlineKeyboardButton(text='Нет',callback_data="Неа")
    markup.add(yes_btn)
    markup.add(no_btn)
    bot.send_message(message.chat.id, "Всё верно?",)

bot.polling()
