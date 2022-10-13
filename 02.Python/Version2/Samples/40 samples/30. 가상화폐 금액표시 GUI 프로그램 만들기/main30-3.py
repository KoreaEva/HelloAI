import tkinter
import tkinter.font

window = tkinter.Tk()
window.title("가상화폐 금액표시")
window.geometry("400x200")
window.resizable(False,False)

font = tkinter.font.Font(size = 30)
label=tkinter.Label(window, text="", font=font)
label.pack()

cnt = 0
def get_coin_1sec():
    global cnt
    now_btc_price = str(cnt)
    cnt = cnt + 1
    label.config(text=now_btc_price)
    window.after(1000,get_coin_1sec)

get_coin_1sec()

window.mainloop()