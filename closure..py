def outer_fun():
    message = "hi"
    
    def inner_fun():
        print(message)  
# message는 inner_func 안에서 정의되지는 않았지만, 안에서 사용되기 때문에 프리변수라고 부른다.       
    return inner_fun()

outer_fun()


def A():
    x = 10
    def B():
        x = 20 # B의 지역변수를 새로 만듬
    B()
    print(x)
A()
# 함수에서 변수를 만들면 항상 현재 함수의 지역 변수가 되기 때문에 10이 출력된다. 


# 현재 함수의 바깥에 있는 지역 변수의 값을 변경하려면 nonlocal 키워드를 사용해야 한다. 
# 50, 400 출력
def A():
    x = 10
    y = 100
    def B():
        x = 20
        def C():
            nonlocal x
            nonlocal y
            x = x + 30
            y = y + 300
            print(x)
            print(y)
        C()
    B()
 
A()


# 함수가 몇 단계든 상관없이 global 키워드를 사용하면 무조건 전역 변수를 사용하게 됩니다.
# 31 출력
x = 1
def A():
    x = 10
    def B():
        x = 20
        def C():
            global x
            x = x + 30
            print(x)
        C()
    B()
 
A()

## closure
# 함수를 둘러싼 환경을 계속 유지하다가 함소를 호출할 때 다시 꺼내서 사용하는 함수를 클로저라고 한다.
def calc():
    a = 3
    b = 5
    def mul_add(x):
        return a * x + b # 바깥쪽에 있는 지역변수 a,b를 사용하여 계산
    #return lambda x: a*x+b 람다식 
    return mul_add 
c = calc() # 클로저
print(c(1),c(2),c(3),c(4),c(5))
