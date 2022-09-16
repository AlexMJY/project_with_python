#  Find out the ID of the bot using token


import telegram # pip install python-telegram-bot

token = '5588890474:AAFqBvlbtVQJ9J8KInCQpaNlpsNIJ7njP2c'
bot = telegram.Bot(token=token)
updates = bot.getUpdates()


for u in updates:
    print(u.message)
    

    
