'''
method의 이름만 존재하는 클래스. 상속받는 클래스에서 강제적으로 메서드를 구현해야 한다. 
'''

from abc import *

class Car(metaclass = ABCMeta):
    @abstractmethod
    def trunk(self):
        pass
    
    def door(self):
        pass
    
    
class Mclaren(Car):
    def trunk(self):
        print("carbon")
        
    def door(self):
        print("steal")
        
my_car = Mclaren()
print(my_car.door())