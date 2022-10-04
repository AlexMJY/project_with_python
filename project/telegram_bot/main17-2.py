# send message

import telegram

token = "5588890474:AAFqBvlbtVQJ9J8KInCQpaNlpsNIJ7njP2c"
id = "856970671"

bot = telegram.Bot(token)
bot.sendMessage(chat_id = id, text = 'controled by python')