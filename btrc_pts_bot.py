import pandas as pd
import datetime
import telebot

token = ""

bot = telebot.TeleBot(token)


#PUT FILE NAME BLOCK
def filename():
    f = "week26.xls"
    return (f)

#CURRENT WEEK BLOCK
def weekdays():
    theday = datetime.date.today()
    weekday = (theday.isoweekday() - 1)
    # The start of the week
    start_date = theday - datetime.timedelta(days=weekday)
    # Finish of the week
    fin_date = start_date + datetime.timedelta(6)
    result = ('неделю с ' + str(start_date) + ' по ' + str(fin_date))
    return result

#HELP BLOCK
HELP = '''
Список доступных команд:
* /start  - Начать работу с расписанием
* /help - Напечатать help
'''

n = 7
work = True


#Написать приветствие Бота
@bot.message_handler(commands=['start'])
def handle_text(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('Александрина')
    user_markup.row('Ефросиния')
    user_markup.row('Павлина')
    user_markup.row('Рагнеда')
    user_markup.row('Янина')
    #bot.send_message(message.from_user.id, 'Текущая неделя с '
    bot.send_message(message.from_user.id, 'Добро пожаловать в бот по получению расписания ПТС!\n Выберите Пункт МЕНЮ', reply_markup=user_markup)


#Функция обработки номера ПТС
@bot.message_handler(func=lambda mess: 'Александрина' == mess.text, content_types=['text'])
def week_aleks(message):
    file = filename()
    xlsx = pd.ExcelFile(file)
    df = pd.read_excel(xlsx, "Лист1")
    send = ('Расписание ПТС Александрина на ' + weekdays() + ' cледующее:\n')
    bot.reply_to(message, send)
    i = 0
    while i < 7:
       day = str(df.loc[i]['Day']) + '\n' + str(df.loc[i]['Александрина'])
       bot.reply_to(message, day)
       i = i + 1

@bot.message_handler(func=lambda mess: 'Ефросиния' == mess.text, content_types=['text'])
def week_efrosinia(message):
    file = filename()
    xlsx = pd.ExcelFile(file)
    df = pd.read_excel(xlsx, "Лист1")
    send = ('Расписание ПТС Ефросиния на ' + weekdays() + ' cледующее:\n')
    bot.reply_to(message, send)
    i = 0
    while i < 7:
        day = str(df.loc[i]['Day']) + str(df.loc[i]['Ефросиния'])
        bot.reply_to(message, day)
        i = i + 1

@bot.message_handler(func=lambda mess: 'Павлина' == mess.text, content_types=['text'])
def week_pavlina(message):
    file = filename()
    xlsx = pd.ExcelFile(file)
    df = pd.read_excel(xlsx, "Лист1")
    send = ('Расписание ПТС Павлина на ' + weekdays() + ' cледующее:\n')
    bot.reply_to(message, send)
    i = 0
    while i < 7:
        day = str(df.loc[i]['Day']) + str(df.loc[i]['Павлина'])
        bot.reply_to(message, day)
        i = i + 1


@bot.message_handler(func=lambda mess: 'Рагнеда' == mess.text, content_types=['text'])
def week_ragneda(message):
    file = filename()
    xlsx = pd.ExcelFile(file)
    df = pd.read_excel(xlsx, "Лист1")
    send = ('Расписание ПТС Рагнеда на ' + weekdays() + ' cледующее:\n')
    bot.reply_to(message, send)
    i = 0
    while i < 7:
        day = str(df.loc[i]['Day']) + str(df.loc[i]['Рагнеда'])
        bot.reply_to(message, day)
        i = i + 1

@bot.message_handler(func=lambda mess: 'Янина' == mess.text, content_types=['text'])
def week_yanina(message):
    file = filename()
    xlsx = pd.ExcelFile(file)
    df = pd.read_excel(xlsx, "Лист1")
    send = ('Расписание ПТС Янина на ' + weekdays() + ' cледующее:\n')
    bot.reply_to(message, send)
    i = 0
    while i < 7:
        day = str(df.loc[i]['Day']) + str(df.loc[i]['Янина'])
        bot.reply_to(message, day)
        i = i + 1

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, HELP)



bot.polling(none_stop = True)
