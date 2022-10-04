from PIL import Image, ImageFilter

# 이미지 불러와서 img 변수에 할당
img = Image.open("C:/Users/jmoon/Desktop/workspace/project_with_python/mini_project/img_edit/pic.jpg")
# img.show()

# print(img.filename)
# print(img.format)
# print(img.size)
# print(img.width)
# print(img.height)
# print(img.mode)

img_resized = img.resize((400, 300))
# img_resized.show()
# img.show()


img_cropped = img.crop((0,0,600,600))
# img_cropped.show()

img_roated = img.rotate(90)
# img_roated.show()

img_flipped_LR = img.transpose(Image.FLIP_LEFT_RIGHT)
# img_flipped_LR.show()

img_flipped_TB = img.transpose(Image.FLIP_TOP_BOTTOM)
# img_flipped_TB.show()

# 편집한 이미지를 저장. ex) 상하반전한 이미지를 저장
# img_flipped_TB.save('pic_flip.jpg')

img_gray = img.convert("L")
# print(img_gray.show())

# 숫자를 높일수록 블러 정도 강해짐
img_blur = img.filter(ImageFilter.GaussianBlur(10))
# print(img_blur.show())

img_edge = img.filter(ImageFilter.EDGE_ENHANCE)
# print(img_edge.show())

