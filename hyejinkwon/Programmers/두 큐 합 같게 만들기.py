# 큐 하나 골라 추출, 다른 큐에 삽입하여 합 같게 ! -> 최소횟수
# pop 1번 insert 1번 ==> 1회 수행

from collections import deque

def solution(queue1, queue2):
    answer = -2
    deque1, sum1 = deque(queue1), sum(queue1)
    deque2, sum2 = deque(queue2), sum(queue2)

    '''
    합이 큰 queue에서 pop하여 작은 queue로 삽입
    sum() 함수 사용 X -> 시간초과
    sum 변수 값으로만 연산 
    '''
    
    for i in range(len(queue1) * 3):
        
        if sum1 > sum2: # queue1 popleft
            sum1 -= deque1[0]
            sum2 += deque1[0]
            deque2.append(deque1.popleft())
            
        elif sum1 < sum2 : # queue2 popleft
            sum2 -= deque2[0]
            sum1 += deque2[0]
            deque1.append(deque2.popleft())
            
        else : # same
            return i
    
    return -1