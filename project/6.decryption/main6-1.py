# 문자열을 순서대로 배열
import itertools

passwd_string = "012345679abcdefhgijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

for len in range(1,4):
    to_attempt = itertools.product(passwd_string, repeat=len)
    for attempt in to_attempt:
        passwd = ''.join(attempt)
        print(passwd)