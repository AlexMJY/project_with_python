#경로에는 절대 경로와 상대 경로가 있다.

#1. 절대경로
#절대적인 기준(최초 디렉토리)으로 경유한 경로를 모두 기입하는 방식이다.
#ex) C:\Users\username\Desktop\~~.txt

#2. 상대경로
#주로 현재 작업하고 있는 폴더를 기준으로 표시
#dot(.) 한개는 하위 디렉토리를, 두개는 상위 디렉토리를 나타낸다.

#파일의 경로가 자주 바뀌거나 최초 디렉토리가 서로 다른 os 모두에서 작동해야 하는 프로그램을
#만드는 경우엔 상대 경로를 이용해야 효율적이다.


import os

# os.getcwd() 현재 작업중인 경로를 문자열로 돌려주는 함수. 
print(os.getcwd())

# os.mkdir() '원하는 경로 + /새로운 디렉토리'를 써주면 새로운 디렉토리 생성 가능
#os.mkdir("Users/jmoon/Destop/test_mkdir")

# os.listdir() 현재 작업 경로에 있는 파일, 디렉토리 리스트 얻기
print(os.listdir(os.getcwd()))

# os.chdir() 원하는 경로를 현재 작업 경로로 변환
# os.chdir("User/jmon/Desktop/")


# os.removedirs() 디렉토리 제거

# os.remove() / os.unlink 파일 제거

# os.rename(path1, path2) 파일 이름 수정. 기존 파일의 경로와 바꾸고자 하는 파일명이 들어간 경로를 입력.



import glob
# 패턴을 사용하여 현재 폴더(디렉토리)는 물론 하위 경로와 파일들을 검색할 때 사용

list_filepath = glob.glob('/Users/jmoon/OneDrive/Pictures/wallpaper/*.jpg')
for filepath in list_filepath:
    print(filepath)
    
    
    
import shutil
# 파일과 폴더를 이동하거나 복사하고 싶을 때 사용하는 모듈

# 상대경로 방식
# shutil.move('이동시킬 파일명.확장자, '파일을 이동시킬 폴더명')

# 절대경로 방식
# shutil.move('이동시킬 파일경로', '파일을 이동시킬 폴더 경로')