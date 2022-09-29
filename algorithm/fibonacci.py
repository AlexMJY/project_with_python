# loop
def fib1(n):
    _curr, _next = 0, 1
    for _ in range(n):
        _curr, _next = _next, _curr + _next
    return _curr

n1 = fib1(5)
print(n1)

# generator
def fib2(n):
    _curr, _next = 0, 1
    for _ in range(n+1):
        yield _curr
        _curr, _next = _next, _curr + _next
        
n2 = fib2(5)
for i, val in enumerate(n2):
    print(f'Fibonacci({i}) : {str(val)}')
    
    
    
# rucursive func
def fib3(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib3(n - 1) + fib3(n - 2)
    
n3 = fib3(5)
print(n3)