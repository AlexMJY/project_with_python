'''
순회 가능, 반복문을 사용할 수 있는 객체를 iterable하다고 한다. 
iter() 내장 함수를 통해 iterable한지 확인 가능
dir() 나장 함수를 통해 __iter__ 메소드가 있으면 iterable

만약 어떤 타입을 만드려고 하는데 이 타입이 반복 가능한 성질을 갖고 있도록 
설계하고자 할 때 바로 이터레이터를 사용
'''

#  __iter__메소드는 이터레이터 객체를 반환해주는데 이터레이터 객체는 __next__ 메소드를 구현하고 있어야 한다.
class MyIterator:
    def __next__(self):
        return 1
    
class MyIterable:
    def __iter__(self):
        obj = MyIterator()
        return obj
    
m = MyIterable()
r = iter(m)
print(next(r))
print(next(r))
print(next(r))



class Season:
    def __init__(self):
        self.data = ['spring', 'summer', 'fall', 'winter']
        self.index = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < len(self.data):
            cur_season = self.data[self.index]
            self.index += 1
            return cur_season
        else:
            raise StopIteration
        
s = Season()
ir = iter(s)
print(next(ir))
print(next(ir))
print(next(ir))
print(next(ir))

# 일반적으로 for문으로 구현하는 게 훨씬 쉽다.