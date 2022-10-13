from gtts import gTTS
from playsound import playsound
import os

#경로를 .py파일의 실행경로로 이동, 현재 경로로 이동
os.chdir(os.path.dirname(os.path.abspath(__file__)))

text = "안녕하세요 마이크로소프트 에이아이 스쿨에 오신 것을 환영합니다. "

tts = gTTS(text=text, lang='ko')
tts.save("hi.mp3")

current_file_path = os.getcwd() + "/hi.mp3"
print(current_file_path)

playsound(current_file_path)