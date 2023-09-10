'''2023.6.8
14:55 ~ 15:07
'''
def solution(topping):
    # Pass1: 토핑 개수 기록
    cake = dict()
    for t in topping:
        if t not in cake:
            cake[t] = 1
        else:
            cake[t] += 1
    # Pass2: 가능한 모든 분할지점에 대해 공평한지 검사
    answer = 0
    b = set() # 동생
    for t in topping:
        # 철수
        cake[t] -= 1
        if cake[t] == 0:
            del cake[t]
        # 동생
        b.add(t)
        if len(cake.keys()) == len(b):
            answer += 1
    return answer
