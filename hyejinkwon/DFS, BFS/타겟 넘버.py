# BFS 이용
from collections import deque

def solution(numbers, target):
    answer = 0
    queue = deque()
    
    # index가 중요
    queue.append([numbers[0], 0])
    queue.append([-1*numbers[0], 0])
    
    while queue :
        value, index = queue.popleft()
        index += 1
        if index < len(numbers) :
            queue.append([value+numbers[index], index])
            queue.append([value-numbers[index], index])
        else : # numbers 리스트 끝까지 다 돌았을 때
            if value == target :
                answer += 1
        
    return answer