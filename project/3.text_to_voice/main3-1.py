# 텍스트를 음성으로 변환
from gtts import gTTS

text = '안녕하세요. 파이썬 작품들입니다.'
tts = gTTS(text=text, lang='ko')
tts.save(r"project\3.text_to_voice\hi.mp3") # 경로 설정후 hi.mp3 생성

