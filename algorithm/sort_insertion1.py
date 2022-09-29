# 삽입 정렬

# list r에서 v가 들어가야 할 위치를 돌려주는 함수
def find_ins_idx(r, v):
    for i in range(0, len(r)):
         # v 값보다 i번 위치에 있는 자료 값이 크면 v가 그 값 바로 앞에 놓여야 정렬 순서가 유지됨
        if v < r[i]:
            return i
        # 위치를 못찾았을 때는 v가 r의 모든 자료보다 크다는 의미이기 때문에 맨 뒤에 삽입
    return len(r)


def ins_sort(a):
    result = []
    while a:
        value = a.pop(0)
        ins_idx = find_ins_idx(result, value)
        result.insert(ins_idx, value)
    return result

d = [2,4,5,1,3]
print(ins_sort(d))
        