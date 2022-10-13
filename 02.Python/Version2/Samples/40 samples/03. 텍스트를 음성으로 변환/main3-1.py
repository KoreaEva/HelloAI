from gtts import gTTS

text = "안녕하세요 마이크로소프트 에이아이 스쿨에 오신 것을 환영합니다. "

tts = gTTS(text=text, lang='ko')
tts.save(r"./hi.mp3")
