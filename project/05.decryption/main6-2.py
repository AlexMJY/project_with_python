import itertools
import zipfile

passwd_string = "012345679abcdefhgijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

zfile = zipfile.ZipFile(r'project\6.decryption\password.zip')

for len in range(1,6):
    to_attempt = itertools.product(passwd_string, repeat=len)
    for attempt in to_attempt:
        passwd = ''.join(attempt)
        print(passwd)
        try:
            zfile.extractall(pwd=passwd.encode())
            print(f'password is {passwd}')
            break
        except:
            pass 