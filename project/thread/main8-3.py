# 다수의 쓰레드를 동작시키는 코드

import threading

def sum(name, value):
    for i in range(0, value):
        print(f'{name} : {i}')
        
t1 = threading.Thread(target=sum, args=(' Thread 1 ', 10))
t2 = threading.Thread(target=sum, args=(' Thread 2 ', 10))

t1.start()
t2.start()

print(' Main Thread ')