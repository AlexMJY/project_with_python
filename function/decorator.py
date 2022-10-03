# @classmethod를 쓰면 인스턴스 내부가 아닌 클래스 전체 관점에서 변수를 다둘 수 있다.
# 즉, class instance 모두가 공유하는 보편적인 값을 설정하고 싶을 때 사용 가능
# (보안적으로 감싸고 싶을 때에도 사용)

from turtle import hideturtle


class Example():
    def met1(self, value):
        self.variable = value
        
    @classmethod
    def met2(self, value):
        self.variable = value
        
        
a = Example()
b = Example()

a.met2(999)
# print(b.variable)


class Member():
    _ins = [] #
    
    def __init__(self, name, height, weight, fat):
        self.name = name
        self.height = height
        self.weight = weight
        self.fat = fat
        
        self.add_instance(self)
        
    @classmethod
    def add_instance(self, ins):
        self._ins.append(ins)
        
a = Member('james', 174, 77, 50)
b = Member('alex', 178,74, 54)
c = Member('mark', 188, 95, 70)
d = Member('peter', 169, 62, 43)

height_mean = sum([m.height for m in Member._ins]) / len(Member._ins)
# print(height_mean)


'''
@property
@property를 붙인 함수는 부를 때 메소드에 괄호를 안붙이고 변수처럼 부를 수 있다.
그렇게 때문에 함수는 argument를 받지 못한다. 

클래스에 정의한 메소드를 변수처럼 불러 사용하고 싶을 때 사용한다.

@이름.setter를 통해 argument를 지정할 수 있다.
'''


class Member2():
    def __init__(self, height, weight, fat):
        self._height = height
        self.weight = weight
        self.fat = fat
        
    @property
    def bmi(self):
        height_in_meter = self._height / 100
        return self.weight/height_in_meter**2
    
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, h):
        if h < 0:
            print("Warning, negative height?")
        self._height = h
    
i = Member2(176, 71, 13)
# print(f'bmi = {i.bmi}')

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

        