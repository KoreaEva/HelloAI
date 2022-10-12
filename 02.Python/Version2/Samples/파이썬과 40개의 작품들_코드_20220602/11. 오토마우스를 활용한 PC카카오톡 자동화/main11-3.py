import pyautogui
import pyperclip
import time
import threading
import os

#경로를 .py파일의 실행경로로 이동, 현재 경로로 이동
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def send_mesaage():
    threading.Timer(10, send_mesaage).start()
    
    picPosition = pyautogui.locateOnScreen('pic1.png')
    print(picPosition)

    if  picPosition is None:
        picPosition = pyautogui.locateOnScreen('pic2.png')
        print(picPosition)

    if  picPosition is None:
        picPosition = pyautogui.locateOnScreen('pic3.png')
        print(picPosition)

    clickPosition = pyautogui.center(picPosition)
    pyautogui.doubleClick(clickPosition)

    pyperclip.copy("이 메세지는 자동으로 보내는 메세지 입니다~~") 
    pyautogui.hotkey("ctrl", "v")
    time.sleep(1.0)

    pyautogui.write(["enter"])
    time.sleep(1.0)

    pyautogui.write(["escape"])
    time.sleep(1.0)

send_mesaage()