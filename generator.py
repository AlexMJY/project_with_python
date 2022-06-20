'''
return 키워드 대신 yield 키워드를 사용하는 함수. yield는 return과 ㄷ르게 
결과값을 돌려주고 실행의 상태를 그대로 저장한 상태로 잠시 멈춘다. 
따라서 나중에 이전에 멈춘 상태에서부터 이어서 코드를 실행할 수 있다. 
'''

def num_gen():
    for i in range(3):
        yield i

g = num_gen()
num1 = next(g)
num2 = next(g)
num3 = next(g)
print(num1, num2, num3)

x = num_gen()
for i in x:
    print(i, end=' ')