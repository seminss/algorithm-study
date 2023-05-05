# 큐에 대기중인 프로세스 중 우선순위가 더 높은 프로세스가 있다면 방금꺼낸걸 다시 큐에 넣음
# 없다면 프로세스 실행. 한번 실행한건 다시 넣지 X

from collections import deque
# any 함수 조건에 해당하는 것이 있는지 없는지 True False

def solution(priorities, location):
    answer = 0
    process = []
    
    # index 값도 같이 저장
    queue = deque([(index,p) for index,p in enumerate(priorities)])
    
    
    while queue :
        max_priority = max(list(p[1] for p in queue))
        index, p = queue.popleft()
        
        if p < max_priority :
            queue.append((index,p))
            
        else :
            answer += 1
            if index == location :
                return answer