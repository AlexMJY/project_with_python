# 10진법에서 n 진법으로 바꾸는 방법

'''
10진법 62를 6진법으로 나타내면?
62 // 6 = 10, 62 % 6 = 2

나눈 몫이 0이 될 때까지 반복

62(10진법) == 142(6진법)
'''

def to_nbase(num, n):
    chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    mod_dict = {i: chars[i] for i in range(len(chars))}
    s = ""
    while num != 0:
        s = mod_dict[num%n] + s
        num //= n
    # print(type(s))
    return s

print(to_nbase(62, 6))
print(to_nbase(255, 16))


# 내장함수로도 가능. 16진법: hex(), 8진법: oct(), 2진법: bin()
print()