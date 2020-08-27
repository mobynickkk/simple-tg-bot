import telebot
from telebot import types

bot = telebot.TeleBot('1266560701:AAGq4ANITk06EVip5uUrlF5g1KP2OTo5xhE')


@bot.message_handler(commands=['start'])
def send_menu(msg):
    markup = types.ReplyKeyboardMarkup(row_width=5)
    markup.add(
        types.KeyboardButton("1", callback_data="position_1"),
        types.KeyboardButton("2", callback_data="position_2"),
        types.KeyboardButton("3", callback_data="position_3"),
        types.KeyboardButton("4", callback_data="position_4"),
        types.KeyboardButton("5", callback_data="position_5")
    )
    bot.send_message(
        msg.chat.id, 
        "Выберите вашу позицию (1 - кери легкой линии, 2 - мидер, 3 - хардлайнер, 4 - семисаппорт, 5 - саппорт)",
        reply_markup=markup
        )




if __name__ == "__main__":
    bot.polling()