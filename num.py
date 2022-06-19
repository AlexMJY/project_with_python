# import time

# def long_task():
#     for i in range(5):
#         time.sleep(1)
#         print(f"workng : {i}")
        
# print("Start")

# for i in range(5):
#     long_task()
    
    
# print("End")

import time
import threading

def long_task():
    for i in range(5):
        time.sleep(1)
        print(f"working{i}")
print('start')

threads = []
for i in range(5):
    t = threading.Thread(target=long_ta)