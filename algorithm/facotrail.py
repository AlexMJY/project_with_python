def fact1(n):
    f = 1
    for i in range(1, n+1):
        f = f * i
    return f


print(fact1(4))


# recursive
def fact2(n):
    if n <= 1:
        return 1
    return n * fact2(n-1)

print(fact2(4))


# find max num with use recursive
# 숫자 n개 중에서 최댓값 찾기를 재귀 호출로 만들어 보세요.
def find_max1(n: list()):
    m = 0
    for i in n:
        if i >= m:
            m = i
    return m

l = [1,4,6,5]
print(find_max1(l))

def find_max2(n: list()):
    
            
        