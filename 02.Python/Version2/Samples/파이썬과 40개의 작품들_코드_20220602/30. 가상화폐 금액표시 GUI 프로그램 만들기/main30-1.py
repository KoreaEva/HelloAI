import tkinter

window = tkinter.Tk()
window.title("가상화폐 금액표시")
window.geometry("400x200")
window.resizable(False,False)

label=tkinter.Label(window, text="hello")
label.pack()

window.mainloop()