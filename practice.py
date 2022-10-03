a, b = 41, "7"

try:
    c = a // b
    d = a % b
    print(f'c = {c}, d = {d}')
    
except Exception as e:
    print("exception")
    
a = [3,4,7,9,'12',13,15]
b = 41
try:
    for i in a:
        c = b // i
        print(f'c = {c}')
except Exception as e:
    print(f'exception, e = {e}')
    print(f'i = {i}')
    
    
    