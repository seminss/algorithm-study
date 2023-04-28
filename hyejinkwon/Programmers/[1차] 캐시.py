from collections import deque

def solution(cacheSize, cities):
    answer = 0
    #queue 이용 : FIFO
    queue = deque()
    
    for c in cities :
        
        if c.lower() in queue :
            # 최신 기록으로 업데이트 : LRU 특징
            queue.remove(c.lower())
            queue.append(c.lower())
            answer += 1
        else :
            queue.append(c.lower())
            answer += 5
        
        if len(queue) > cacheSize :
            queue.popleft()
    return answer