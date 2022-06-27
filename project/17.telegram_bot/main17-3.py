# 자동응답 코드

import telegram
from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters

token = "5588890474:AAFqBvlbtVQJ9J8KInCQpaNlpsNIJ7njP2c"
id = "856970671"

bot = telegram.Bot(token)
bot.sendMessage(chat_id = id, 
                text = 'This is an automatic response test. Please enter "Hello World" or "Hi"')

updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher
updater.start_polling()

def handler(update, context):
    user_text = update.message.text
    if user_text == 'Hello World':
        bot.send_message(chat_id = id, text = "Welcome!")
    elif user_text == 'HI':
        bot.send_message(chat_id = id, text = "Hi Bro~")
        
echo_hanlder = MessageHandler(Filters.text, handler)
dispatcher.add_handler(echo_hanlder)
        