import telegram

token = "2147448681:AAF54C5_5U7nKqwKvwnbI9n4Dr6m5GmicbY"
id = "730238165"

bot = telegram.Bot(token)
bot.sendMessage(chat_id=id, text="파이썬으로 보내는 메시지 입니다.")