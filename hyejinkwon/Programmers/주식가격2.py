# 가격이 떨어지지 않은 기간 : 몇 초

from collections import deque

def solution(prices):
    answer = []
    prices_queue = deque(prices)
    
    while prices_queue:
        p = prices_queue.popleft()
        test = 0
        for q in prices_queue :
            if p > q :
                test+=1
                break
            test += 1
        answer.append(test)
    
    return answer

# 효율성 테스트 최대 89ms