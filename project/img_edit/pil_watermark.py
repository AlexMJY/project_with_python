from PIL import Image, ImageDraw, ImageFont

# 워터마크 삽입할 이미지 불러오기
img = Image.open("C:/Users/jmoon/Desktop/workspace/project_with_python/mini_project/img_edit/pic.jpg")
width, height = img.size

# 그림판에 이미지를 그대로 붙여넣는 느낌의 Draw() 함수
draw = ImageDraw.Draw(img)

# 삽입합 워터마크 문자
text = 'source_edward'

# 삽입할 문자의 폰트 설정
font = ImageFont.truetype("C:/WINDOWS/FONTS/LSANS.TTF", 30)

# 삽입할 문자의 높이, 너비 정보 가져오기
width_txt, height_txt = draw.textsize(text, font)

# 워터마크 위치 설정
margin = 10
x = width - width_txt - margin
y = height - height_txt - margin

# 텍스트 적용하기
draw.text((x, y), text, fill='white', font=font)

# 이미지 출력
img.show()


