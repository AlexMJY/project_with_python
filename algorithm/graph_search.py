fr_info = {
    'Summer': ['John', 'Justin', 'Mike'],
    'John': ['Summer', 'Justin'],
    'Justin': ['John', 'Summer', 'Mike', 'May'],
    'Mike': ['Summer', 'Justin'],
    'May': ['Justin', 'Kim'],
    'Kim': ['May'],
    'Tom': ['Jerry'],
    'Jerry': ['Tom']
}

'''
1) 처리할 사람을 저장할 queue를 만든다.
2) 이미 큐에 추가한 사람을 저장할 집합(done)을 만든다
3) 검색의 출발점이 될 사람을 큐와 집합에 추가한다.
4) 큐에 사람이 남아 있다면 큐에서 처리할 사람을 꺼낸다.
5) 꺼낸 사람을 출력한다.
6) 꺼낸 사람의 친구들 중 아직 큐에 추가된 적이 없는 사람을 골라 큐와 집합에 추가합니다.
7) 큐에 처리할 사람이 남아 있다면 4번 과정부터 다시 반복한다.
''' 

def print_all_friends(g, start):
    # g = graph
    
    qu = []
    done = set()
    
    
    qu.append(start) # 자신을 큐에 넣고 시작
    done.add(start) # 집합에도 추가
    
    while qu:
        p = qu.pop(0)
        print(p)
        
        for x in g[p]:
            if x not in done:
                qu.append(x)
                done.add(x)
                
                
print_all_friends(fr_info, "Summer")
print()
print_all_friends(fr_info, "Jerry")



def print_all_friends_intimacy(g, start):
    qu = []
    done = set()
    
    qu.append((start, 0)) # (사람이름, 친밀도) 정보를 튜플로 묶어 처리
    done.add(start)
    
    while qu:
        (p, d) = qu.pop(0)
        print(p, d)
        for x in g[p]:
            if x not in done:
                qu.append((x, d+1))
                done.add(x)

print_all_friends_intimacy(fr_info, "Summer")
print()
print_all_friends_intimacy(fr_info, "Jerry")