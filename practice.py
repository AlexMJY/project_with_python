# 표준 체중 구하기
def std_weight(height, gender):
    if gender == "male":
        return height * height * 22
    else:
        return height * height * 21
    
    
    
height = 175
gender = "male"
weight = std_weight(height / 100, gender)
weight = round(weight, 2)
print(f"키 {height}cm {gender}의 표준 체중은 {weight}kg입니다.")