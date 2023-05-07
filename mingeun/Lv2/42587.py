''' 2023.5.4
20:12 ~ 20:45
'''
from heapq import heappush, heappop
from collections import deque
def solution(priorities, location):
    n= len(priorities) # 프로세스 개수
    processes = deque([p for p in range(n)])
    max_heap = []
    for p in priorities:
        heappush(max_heap, -p)
    answer = 0
    while processes:
        pid = processes.popleft()
        # 해당 프로세스 종료
        if -priorities[pid] == max_heap[0]:
            answer += 1
            heappop(max_heap)
            if pid == location:
                return answer;
        else:
            processes.append(pid)
                
    return answer
