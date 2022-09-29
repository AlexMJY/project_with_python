'''
크기가 다른 n개의 원반이 있고 세 개의 기둥이 있다. 왼쪽 기둥에 있는 원반을 모두 오른쪽으로 옮겨야 한다. 
크기가 더 큰 원반은 위에 있을 수 없고, 한 번에 한 개씩만 옮길 수 있고, 각 기둥의 맨 위 원반을 옮겨야 한다.

1. 원반이 한 개면 한 번에 옮기고 끝 (종료 조건)
2. n개 있을 땐, n개 원반 중 n-1개를 2번 기둥으로 옮깁니다. 
3. 1번에 남아있는 가장 큰 원반을 3번 기둥으로 옮깁니다.
4. 2번 기둥에 있는 n-1개의 원반을 다시 3번 기둥으로 옮깁니다. (1번 보조기둥 사용)
'''
# n: 원반 개수, from_pos: 출발점 기둥, to_pos: 도착점 기둥, aus_pos: 보조 기둥
def hanoi(n, from_pos, to_pos, aux_pos):
    if n == 1:
        print(from_pos, "→", to_pos)
        return
    
    # 원반 n-1개를 aux_pos로 이동
    hanoi(n-1, from_pos, aux_pos, to_pos)
    
    # 가장 큰 원반을 목적지로 이동
    print(from_pos, "→", to_pos)
    
     # aux_pos에 있는 원반 n-1개를 목적지로 이동(from_pos를 보조 기둥으로)
    hanoi(n-1, aux_pos, to_pos, from_pos)

print("n = 1")
hanoi(1, 1, 3, 2) # 원반 한 개를 1번 기둥에서 3번 기둥으로 이동(2번을 보조 기둥으로)
print("n = 2")
hanoi(2, 1, 3, 2) # 원반 두 개를 1번 기둥에서 3번 기둥으로 이동(2번을 보조 기둥으로)
print("n = 3")
hanoi(3, 1, 3, 2) # 원반 세 개를 1번 기둥에서 3번 기둥으로 이동(2번을 보조 기둥으로)