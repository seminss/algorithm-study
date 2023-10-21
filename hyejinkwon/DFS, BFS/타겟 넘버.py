# BFS 이용
from collections import deque

def solution(numbers, target):
    answer = 0
    queue = deque()
    queue.append([numbers[0], 0])
    queue.append([numbers[0]*-1, 0])
    
    while queue :
        val, i = queue.popleft()
        i += 1
        
        if i < len(numbers) :
            queue.append([val + numbers[i], i])
            queue.append([val - numbers[i], i])
        else :
            if val == target : answer += 1
    
    return answer