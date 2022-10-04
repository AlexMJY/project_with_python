from time import sleep

def square(x):
    sleep(0.001)
    return x**2


from multiprocessing import Pool, cpu_cou nt
from time import time


n_cpu = cpu_count()
print(f"n_cpu = {n_cpu}")

p = Pool(n_cpu - 1)

start = time()
for s in p.imap(square, range(900)):
    print(f's: {s}', end='')
end = time()