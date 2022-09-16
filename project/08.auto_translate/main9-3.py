# 영어 문서를 한글로 번역

import googletrans
from os import linesep

translator = googletrans.Translator()

read_file_path = r"project\09.auto_translate\eng_file.txt"

with open(read_file_path, 'r') as f:
    readLines = f.readlines()
    
for lines in readLines:
    result1 = translator.translate(lines, dest = 'ko')
    print(result1.text)
    
    
# error