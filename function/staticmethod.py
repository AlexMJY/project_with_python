'''
@staticmethod : 메서드를 정적 메서드로 변환한다. 
정적 메서드는 묵시적인 첫 번째 인자를 받지 않는다. 
즉, 인스턴스 변수에 접근할 수 없다. (메서드 안의 변수, 클래스 변수와 다름) 
자기 자신 인스턴스도 가리킬 수 없기 때문에 self argument를 받지 않고,
바로 알고리즘에 사용될 argument를 입력 받는다.

클래스 안의 독립적인 함수(메서드)라고 생각하면 편하다.
'''

@staticmethod
def set_h(mew_height):
    self.h = new_height ### error