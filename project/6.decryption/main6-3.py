# 비밀번호를 찾으면 프로그램이 종료되는 코드

import itertools
import zipfile

def un_zip(passwd_string, min_len, max_len, zfile):
    for len in range(min_len, max_len+1):
        to_attempt = itertools.product(passwd_string, repeat=len)
        for attempt in to_attempt:
            passwd = ''.join(attempt)
            print(passwd)
            
            try:
                zfile.extractall(pwd=passwd.encode())
                print(f' password is {passwd}')
                return 1
            except:
                pass
            
passwd_string = '012345679abcdefhgijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

zfile = zipfile.ZipFile(r'project\6.decryption\password.zip')

min_len = 1
max_len = 5

unzip_result = un_zip(passwd_string, min_len, max_len, zfile)
if unzip_result == 1:
    print('mission complete')
else:
    print('fail')    