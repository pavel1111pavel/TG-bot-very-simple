import telebot

from telebot import types

bot = telebot.TeleBot('7852553113:AAFLGaJ0Hha5FFgctIKu5cirqCOqZRn1R8E')

menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
answer = types.KeyboardButton("Ответ")
test = types.KeyboardButton("Тест")
menu.add(answer, test)

@bot.message_handler(commands=['start'])
def start_message(message):
  bot.send_message(chat_id=message.chat.id , text="Привет!", reply_markup = menu)
  
webhook_info = bot.get_webhook_info()
if webhook_info.url:
    bot.delete_webhook()
    print("Deleted existing webhook")
bot.polling()
