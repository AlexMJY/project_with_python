import re

p = re.compile("ca.e")
# m = p.match("case")
# print(m.group()) # 매치되지 않으면 에러 발생

def print_match(m):
    if m:
        print("group():", m.group()) # 일치하는 문자열 반환
        print("string():", m.string) # 입력받은 문자열 반환
        print("start():", m.start()) # 일치하는 문자열의 시작 index
        print("end():", m.end()) # 일치하는 문자열의 끝 index
        print("span():", m.span()) # 일치하는 문자열의 시작과 끝 index
    else:
        print("not matched")
        
# m1 = p.match('careless') # match: 주어진 문자열의 처음부터 일치하는지 확인
# print_match(m1)

# m2 = p.search("good care") # search: 주어진 문자열 중에 일치하는 게 있는지 확인
# print_match(m2)

m3 = p.findall("good care cafe") # findall: 일치하는 모든 것을 리스트 형태로 반환
print(m3)