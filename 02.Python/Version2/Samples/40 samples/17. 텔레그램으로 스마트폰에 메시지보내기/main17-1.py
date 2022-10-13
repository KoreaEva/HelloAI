import telegram

token = '2147448681:AAF54C5_5U7nKqwKvwnbI9n4Dr6m5GmicbY'
bot = telegram.Bot(token=token)
updates = bot.getUpdates()
for u in updates:
    print(u.message)