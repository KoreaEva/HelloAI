import pyautogui
import time
import pyperclip

pyautogui.moveTo(1241,206,0.2)
pyautogui.click()
time.sleep(0.5)

pyperclip.copy("서울 날씨") 
pyautogui.hotkey("ctrl", "v")
time.sleep(0.5)

pyautogui.write(["enter"]) 
time.sleep(1)

start_x = 992
start_y = 220
end_x = 1656
end_y = 635

pyautogui.screenshot(r'10. 오토마우스를 활용한 웹페이지 자동화\서울날씨.png', region=(start_x, start_y, end_x-start_x, end_y-start_y))
