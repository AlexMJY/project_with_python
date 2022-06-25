'''
두가지 동작 동시에 실행
main action은 2초마다, thread_1은 1초마다 실행
'''

import threading
import time

def thread_1():
    while True:
        print("thread action 1")
        time.sleep(1.0)
        
t1 = threading.Thread(target=thread_1)
t1.start()

while True:
    print('main action')
    time.sleep(2.0)