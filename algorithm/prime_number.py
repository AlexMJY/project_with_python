# def is_prime(num):
#     if num == 1:
#         return False
#     for i in range(2, num):
#         if num % 1 == 0:
#             return False
#     return True

def is_prime2(num):
    if num == 1: 
        return False
    for i in range(2, int(num**(1/2))+1):
        if num % i == 0:
            return False
    return True
# num의 루트까지만 보겠다는 의미. 만약 넘버가 9만이면 300번만 돌면 된다.
# 만약 소수를 구하는 과정에서 나누어 떨어지는 수가 있으면,
# 나누어 떨어지는 수는 무조건 쌍이 존재한다.
# 쌍이 되는 숫자는 루트 num보다 큰 쪽에 존재한다. 
# 만약 18이 들어오면 (2,9), (3,6) 쌍이 존재한다
# 루트 18은 쌍의 가운데에 존재하고 2와 3만 체크하면 된다.
# https://www.youtube.com/watch?v=LD-Px5YCd8Y



# print(is_prime(901256437))
print(is_prime2(901256437))