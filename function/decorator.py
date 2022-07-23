# 데코레이터는 기존 함수를 수정하지 않으면서 추가 기능을 구현할 때 사용한다.
# 일반적인 함수
from textwrap import wrap


def trace1(func):
    def wrapper():
        print(func.__name__, 'function start')
        func()
        print(func.__name__, 'function end')
    return wrapper

def hello1():
    print("hello")
def world1():
    print("world")

trace_hello1 = trace1(hello1)
trace_hello1()
trace_world1 = trace1(world1)
trace_world1()

# @ decorator 사용
def trace2(func):
    def wrapper():
        print(func.__name__, 'function start')
        func()
        print(func.__name__, 'function end')
    return wrapper

@trace2
def hello2():
    print("hello")

@trace2
def world2():
    print("world")
    
hello2()
world2()


# ex1 매개변수 처리
def trace3(func):
    def wrapper(a, b):
        r = func(a, b)
        print(f'{func.__name__} (a={a}, b={b}) -> {r}')
        return r
    return wrapper

@trace3
def add(a,b):
    return a + b
print(add(10, 20))

        
# 클래스 데코레이터
class Trace:
    def __init__(self, func):
        self.func = func
        
    def __call__(self):
        print(self.func.__name__, 'function start')
        self.func()
        print(self.func.__name__, 'function end')

@Trace
def hello():
    print('hello')
hello()

        