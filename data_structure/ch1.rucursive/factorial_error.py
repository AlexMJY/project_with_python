def factorial(n):
    return factorial(n-1) * n # 1

if __name__ == "__main__":
    for i in range(1, 6):
        print(factorial(i)) # 2