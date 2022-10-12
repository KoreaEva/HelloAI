import tkinter
import tkinter.font
import pyupbit
import threading
import time

coin_price = 0
def get_coin_price():
    global coin_price
    while True:
        coin_price = pyupbit.get_current_price("KRW-BTC")
        time.sleep(1.0)
        
t1 = threading.Thread(target=get_coin_price)
t1.daemon = True
t1.start()

window = tkinter.Tk()
window.title("비트코인 실시간 가격")
window.geometry("400x50")
window.resizable(False,False)

font = tkinter.font.Font(size = 30)
label=tkinter.Label(window, text="", font=font)
label.pack()

def get_coin_1sec():
    global coin_price
    now_btc_price = str(coin_price)
    label.config(text=now_btc_price)
    window.after(1000,get_coin_1sec)

get_coin_1sec()

window.mainloop()