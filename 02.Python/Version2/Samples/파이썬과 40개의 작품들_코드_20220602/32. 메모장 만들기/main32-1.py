from tkinter import *
from tkinter.filedialog import *


def new_file():
    pass

def save_file():
    pass

def maker():
    pass

window = Tk()
window.title("메모장")
window.geometry("400x400+800+300")
window.resizable(False, False)

menu = Menu(window)
menu_1 = Menu(menu, tearoff=0)
menu_1.add_command(label="새파일", command=new_file)
menu_1.add_command(label="저장", command=save_file)
menu_1.add_separator()
menu_1.add_command(label="종료", command=window.destroy)
menu.add_cascade(label="파일", menu=menu_1)

menu_2 = Menu(menu, tearoff=0)
menu_2.add_command(label="만든이", command = maker)
menu.add_cascade(label="만든이", menu=menu_2)

window.config(menu=menu)

window.mainloop()