# 최대 2명 탑승 + 무게 제한

from collections import deque

def solution(people, limit):
    answer = 0
    q = deque(people)
    q = deque(sorted(q))
    # 가장 작은 무게 + 가장 큰 무게
    
    while len(q) > 1 :
        if q[0] + q[-1] <= limit :
            q.pop() # 가장 큰 무게 빼기
            q.popleft() # 가장 작은 무게 빼기
            answer += 1
        else :
            q.pop() # 합 limit 넘어가면 큰 무게 빼기
            answer += 1
    
    if len(q) == 1 :
        answer += 1
    
    return answer