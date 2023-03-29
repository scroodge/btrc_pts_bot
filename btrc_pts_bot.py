import pandas as pd
import datetime
import telebot

token = "YOUR TELEGRAM TOKEN"


bot = telebot.TeleBot(token)

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
    url = ('pandas.html')
    dfs = pd.read_html(url, encoding='utf8', keep_default_na=False)
    send = ('Расписание на ' + weekdays() + ' для')
    bot.reply_to(message, send)
    i = 0
    while i <= 7:
       day = (str(dfs[0][0][i]) + '\n' + str(dfs[0][1][i]))
       bot.reply_to(message, day)
       i = i + 1

@bot.message_handler(func=lambda mess: 'Ефросиния' == mess.text, content_types=['text'])
def week_efrosinia(message):
    url = ('pandas.html')
    dfs = pd.read_html(url, encoding='utf8', keep_default_na=False)
    send = ('Расписание на ' + weekdays() + ' для')
    bot.reply_to(message, send)
    i = 0
    while i <= 7:
        day = (str(dfs[0][0][i]) + '\n' + str(dfs[0][2][i]))
        bot.reply_to(message, day)
        i = i + 1

@bot.message_handler(func=lambda mess: 'Павлина' == mess.text, content_types=['text'])
def week_pavlina(message):
    url = ('pandas.html')
    dfs = pd.read_html(url, encoding='utf8', keep_default_na=False)
    send = ('Расписание на ' + weekdays() + ' для')
    bot.reply_to(message, send)
    i = 0
    while i <= 7:
        day = (str(dfs[0][0][i]) + '\n' + str(dfs[1][1][i]))
        bot.reply_to(message, day)
        i = i + 1


@bot.message_handler(func=lambda mess: 'Рагнеда' == mess.text, content_types=['text'])
def week_ragneda(message):
    url = ('pandas.html')
    dfs = pd.read_html(url, encoding='utf8', keep_default_na=False)
    send = ('Расписание на ' + weekdays() + ' для')
    bot.reply_to(message, send)
    i = 0
    while i <= 7:
        day = (str(dfs[0][0][i]) + '\n' + str(dfs[1][2][i]))
        bot.reply_to(message, day)
        i = i + 1

@bot.message_handler(func=lambda mess: 'Янина' == mess.text, content_types=['text'])
def week_yanina(message):
    url = ('pandas.html')
    dfs = pd.read_html(url, encoding='utf8', keep_default_na=False)
    send = ('Расписание на ' + weekdays() + ' для')
    bot.reply_to(message, send)
    i = 0
    while i <= 7:
        day = (str(dfs[0][0][i]) + '\n' + str(dfs[2][1][i]))
        bot.reply_to(message, day)
        i = i + 1

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, HELP)



bot.polling(none_stop = True)
