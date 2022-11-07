import os

# os.path.join()
# 최소 하나 이상의 문자열을 집어넣으면 그것들을 경로명으로 인식해서 합춰준다.
# os랑 상관없이 디렉터리 경로를 설정할 수 있다.
os.path.join("비둘기", "직박구리", "느시")


# os.makedirs
# os.mkdirs는 만들려는 폴더가 이미 있으면 에러 발생. makedirs는 exist_ok=True 설정하면 됨.
os.makedirs("folder")
os.makedirs("비둘기/직박구리/folder")