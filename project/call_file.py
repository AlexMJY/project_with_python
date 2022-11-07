# 파일 이름이 규칙성 있다면 for문으로 부르면 된다
paths = [f'c://user/desktop/{i}' for i in range(1, 50)]

# 파일 이름이 중구난방일 경우 glob('*.sav') 함수를 사용한다
from glob import glob
lists = glob("randomname/*.jpg") # 확장자 jpg


# 여러 경로에 있는 파일을 불러올 때 os.walk() 사용
import os
for items in os.walk('datadir'):
    print(items)
    
path = []
for folder, _, files in os.walk("datadir"):
    for file in files:
        if ".png" in file:
            path.append(folder + "/" + file)
