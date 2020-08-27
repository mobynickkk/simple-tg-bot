import telebot
from telebot import types

bot = telebot.TeleBot('1266560701:AAGq4ANITk06EVip5uUrlF5g1KP2OTo5xhE')


@bot.message_handler(commands=['start'])
def send_menu(msg):
    markup = types.ReplyKeyboardMarkup(row_width=5)
    markup.add(
        types.KeyboardButton("1"),
        types.KeyboardButton("2"),
        types.KeyboardButton("3"),
        types.KeyboardButton("4"),
        types.KeyboardButton("5")
    )
    bot.send_message(
        msg.chat.id, 
        "Выберите вашу позицию (1 - кери легкой линии, 2 - мидер, 3 - хардлайнер, 4 - семисаппорт, 5 - саппорт)",
        reply_markup=markup
    )
    bot.register_next_step_handler(msg, get_range)


def get_range(msg):
    position = msg.text
    markup = types.ReplyKeyboardMarkup(row_width=2)
    markup.add(
        types.KeyboardButton("Ближний бой"),
        types.KeyboardButton("Дальний бой")
    )
    bot.send_message(
        msg.chat.id,
        "Выберите, какой тип героя для вас больше подходит",
        reply_markup=markup
    )






if __name__ == "__main__":
    bot.polling()