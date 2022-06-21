from gtts import gTTS
from playsound import playsound

file_path = r'project\3.text_to_voice\my_text.txt'
with open(file_path, 'rt', encoding= 'UTF8') as f:
    read_file = f.read()
    
tts = gTTS(text=read_file, lang='ko')
tts.save(r"project\3.text_to_voice\my_text.mp3")
