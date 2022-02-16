import telegram

from constants import KEY

bot = telegram.Bot(token=KEY)

updates = bot.get_updates()
print(updates[0])


#bot.send_message(text='Hi John!', chat_id=619176048)