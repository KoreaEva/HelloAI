from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import telegram
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

send_message_list = []

while True:
    try:
        driver.get(url='https://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu')
        driver.implicitly_wait(time_to_wait=10)
        titles = driver.find_elements_by_css_selector('#revolution_main_table > tbody > tr > td:nth-child(3) > table > tbody > tr > td:nth-child(2) > div > a > font')
        urls = driver.find_elements_by_css_selector('#revolution_main_table > tbody > tr > td:nth-child(3) > table > tbody > tr > td:nth-child(2) > div > a')

        message = ""
        for i in range(len(titles)):
            if "김치" in titles[i].text:
                message = titles[i].text + "\n" +urls[i].get_attribute('href')
                if message not in send_message_list:
                    print(message)
                    send_message_list.append(message)
                    token = "2147448681:AAF54C5_5U7nKqwKvwnbI9n4Dr6m5GmicbY"
                    id = "730238165"
                    bot = telegram.Bot(token)
                    bot.sendMessage(chat_id=id, text=message)
                    
        time.sleep(60.0 * 5)
        
    except KeyboardInterrupt:
        break