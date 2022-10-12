from gtts import gTTS

text = "안녕하세요. 파이썬과 40개의 작품들 입니다."

tts = gTTS(text=text, lang='ko')
tts.save(r"3. 텍스트를 음성으로 변환\hi.mp3")
