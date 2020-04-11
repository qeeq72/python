import telebot

bot = telebot.TeleBot("")


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    msg = bot.send_message(message.chat.id, 'Привет! Я codex_bot!')


@bot.message_handler(commands=['auth'])
def send_auth(message):
    pass


bot.polling()
