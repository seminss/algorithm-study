'''2023.6.16
12:43 ~ 13:13
'''
from collections import deque
def solution(order):
    '''
    1 2 3 4 5 -> 4 3 1 2 5
    '''
    answer = 0
    q = deque(order)
    stack = []
    n = len(order)
    for i in range(1, n+1):
        # 바로 트럭에 싣는다.
        if q[0] == i:
            answer += 1
            q.popleft()
            # 보조 벨트에서 뺀다.
            while len(stack)>0 and stack[-1] == q[0]:
                stack.pop()
                q.popleft()
                answer+= 1
        # 보조 벨트에 넣는다.
        else:
            stack.append(i)
            
    return answer
