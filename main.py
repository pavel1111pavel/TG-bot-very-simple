import telebot

from telebot import types

bot = telebot.TeleBot('7852553113:AAFLGaJ0Hha5FFgctIKu5cirqCOqZRn1R8E')

menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
answer = types.KeyboardButton("Ответ")
test = types.KeyboardButton("Тест")
test_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
test_answer = types.KeyboardButton("Еще один тест")
test_answer_more = types.KeyboardButton("Вот такая кнопка")
menu.add(answer, test)
test_menu.add(test_answer, test_answer_more)

@bot.message_handler(commands=['start'])
def start_message(message):
  bot.send_message(chat_id=message.chat.id , text="Привет!", reply_markup = menu)

@bot.message_handler(func=lambda message: message == 'Тест')
def test_message(message):
  bot.send_message(chat_id=message.chat.id , text="Возможно, тут будет реклама", reply_markup = test_menu)
  
webhook_info = bot.get_webhook_info()
if webhook_info.url:
    bot.delete_webhook()
    print("Deleted existing webhook")
bot.polling()
