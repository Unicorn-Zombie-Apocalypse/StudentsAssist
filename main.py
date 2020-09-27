import telebot
from telebot import types

global str
import sqlite3

otv = ""
login = ""
pas = ""

login = str(login)
pas = str(pas)

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
    bot.send_message(message.chat.id, "==============================================================")
    bot.send_message(message.chat.id, "https://www.severcart.ru/blog/all/python_sqlite3/")
    bot.send_message(message.chat.id, "==============================================================")
    bot.send_message(message.chat.id, "https://tlgrm.ru/docs/bots/api")
    bot.send_message(message.chat.id, "==============================================================")
    bot.send_message(message.chat.id, "https://sebastianraschka.com/Articles/2014_sqlite_in_python_tutorial.html")


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'привет':
        bot.send_message(message.chat.id, 'Привет, мой создатель')
        bot.send_message(message.chat.id, )
    if message.text == 'тест':
        bot.send_message(message.chat.id, str(message.text()))
    elif message.text == 'пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')

    # вход
    if message.text == 'Вход':
        hide_keyboard = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, 'Введи логин', reply_markup=hide_keyboard)
        bot.register_next_step_handler(message, get_login)

    if message.text == 'Регистрация':
        hide_keyboard = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, 'Выбери свой логин', reply_markup=hide_keyboard)
        bot.register_next_step_handler(message, reg_login)

    if message.chat.id == 480718174:
        if message.text == 'Мне грустно':
            bot.send_message(message.chat.id, "Не обижайся сладкая булочка,ты лучший")
    print(message.chat.id, message.text)


def get_login(message):
    global login
    login = message.text
    hide_keyboard = types.ReplyKeyboardRemove()
    bot.send_message(message.from_user.id, "Какой пароль?", reply_markup=hide_keyboard)
    bot.register_next_step_handler(message, get_pas)


def get_pas(message):
    global pas
    pas = message.text

    bot.send_message(message.from_user.id, "Твой логин " + str(login))
    bot.send_message(message.from_user.id, "Твой пароль " + str(pas))

    markup = types.InlineKeyboardMarkup(row_width=1)
    yes_btn = types.InlineKeyboardButton(text='Да', callback_data="Да")
    no_btn = types.InlineKeyboardButton(text='Нет', callback_data="Неа")
    markup.add(yes_btn)
    markup.add(no_btn)
    bot.send_message(message.chat.id, "Всё верно?", reply_markup=markup)







def reg_login(message):
    bd = sqlite3.connect(r'./Logins/bd')
    cursor = bd.cursor()
    cursor.execute("""SELECT * FROM logins WHERE ID LIKE '{sravnenie}' """.format(sravnenie=str(message.chat.id)))
    if str(srav) == "[]":
        print("Create User")
        cursor.execute("""INSERT INTO logins (ID) VALUES (?)""", [message.chat.id])
    cursor.execute("""UPDATE logins SET login = "{log}" where id = {id}""".format(log=message.text, id=message.chat.id))
    print("update")
    bd.commit()
    bot.send_message(message.chat.id, "Ваш пароль?")
    bot.register_next_step_handler(message, reg_pas)


def reg_pas(message):
    bd = sqlite3.connect(r'./Logins/bd')
    cursor = bd.cursor()
    cursor.execute("""SELECT * FROM logins WHERE ID LIKE '{sravnenie}' """.format(sravnenie=str(message.chat.id)))
    cursor.execute("""UPDATE logins SET password = "{pas}" where id = {id}""".format(pas=message.text, id=message.chat.id))
    print(srav)
    bd.commit()
    bot.send_message(message.chat.id,"Ваше имя? (Не никнейм)")
    bot.register_next_step_handler(message, reg_name)


def reg_name(message):
    bd = sqlite3.connect(r'./Logins/bd')
    cursor = bd.cursor()
    cursor.execute("""SELECT * FROM logins WHERE ID LIKE '{sravnenie}' """.format(sravnenie=str(message.chat.id)))
    cursor.execute("""UPDATE logins SET name = "{name}" where id = {id}""".format(name=message.text, id=message.chat.id))
    print("update")
    bd.commit()
    bot.send_message(message.chat.id, "Ваша фамилия? (Не никнейм)")
    bot.register_next_step_handler(message, reg_surname)


def reg_surname(message):
    bd = sqlite3.connect(r'./Logins/bd')
    cursor = bd.cursor()
    cursor.execute("""SELECT * FROM logins WHERE ID LIKE '{sravnenie}' """.format(sravnenie=str(message.chat.id)))
    cursor.execute("""UPDATE logins SET surname = "{surname}" where id = {id}""".format(surname=message.text, id=message.chat.id))
    print("update")
    bd.commit()
    bot.send_message(message.chat.id, "Всё готово")


bot.polling()
