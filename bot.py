import telebot

bot = telebot.Telebot('1266560701:AAGq4ANITk06EVip5uUrlF5g1KP2OTo5xhE')

@bot.message_handler(commands=['start'])
def menu(message):
    pass