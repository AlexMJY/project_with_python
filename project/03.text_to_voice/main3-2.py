# 코드에서 바로 음성
from gtts import gTTS
from playsound import playsound

text = '안녕하세요. 서울에 사는 에드워드문입니다.'

tts = gTTS(text=text, lang='ko')
tts.save(r"project\3.text_to_voice\hi.mp3")
playsound(r"project\3.text_to_voice\hi.mp3")