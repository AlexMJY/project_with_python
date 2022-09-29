# 퀵 정렬
# pivot을 어떻게 정하느냐에 따라 성능 차이가 심하다. 최악일 경우 O(n^2), 평균적으로 O(nlogn)
from asyncio import QueueEmpty


def quick_sort(a):
    n = len(a)
    
    if n <= 1:
        return a
    
    pivot = a[-1]
    g1 = []
    g2 = []
    
    for i in range(0, n-1):
        if a[i] < pivot:
            g1.append(a[i])
        else:
            g2.append(a[i])
            
    return quick_sort(g1) + [pivot] + quick_sort(g2)

d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
print(quick_sort(d))