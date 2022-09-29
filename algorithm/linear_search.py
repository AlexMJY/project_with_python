def linear_search(l: list(), s: tuple()):
    for i, v in enumerate(l):
        if v in s:
            print(i, end=' ')
            
            
l1 = [17, 92, 18, 33, 58, 5, 33, 42]
l2 = (18, 33, 900)

print(linear_search(l1, l2))


# 학생 번호 찾기
def search_name(no, na):
    di = {}
    for i, v in zip(no, na):
        di[i] = v
        
    s_num = int(input("학생 번호: "))
    return di[s_num]
    
    
stu_no = [39, 14, 67, 105]
stu_name = ["Justin", "John", "Mike", "Summer"]

print(search_name(stu_no, stu_name))