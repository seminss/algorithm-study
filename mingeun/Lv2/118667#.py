''''2023.6.16
15:25 ~ 16:24
'''
from collections import deque
def solution(queue1, queue2):
    s1 = sum(queue1)
    s2 = sum(queue2)
    q1 = deque(queue1)
    q2 = deque(queue2)
    total = s1 + s2
    x = total//2
    op = 0 # 작업 횟수
    if (s1+s2)%2 != 0:
        return -1
    while op < 3*len(queue1):
        # print(f'q1: {q1} s1: {s1} q2: {q2} s2: {s2}')
        if s1 == x:
            return op
        # 큐의 합 > x -> 빼야됨
        elif s1 > x:
            m = q1.popleft()
            s1 -= m
            q2.append(m)
            s2 += m
        # 큐의 합 < x -> 추가야됨
        elif s1 < x:
            m = q2.popleft()
            s2 -= m
            q1.append(m)
            s1 += m
        op += 1
    return -1''2023.6.16
15:25 ~ 16:24
'''
from collections import deque
def solution(queue1, queue2):
    s1 = sum(queue1)
    s2 = sum(queue2)
    q1 = deque(queue1)
    q2 = deque(queue2)
    total = s1 + s2
    x = total//2
    op = 0 # 작업 횟수
    if (s1+s2)%2 != 0:
        return -1
    while op < 3*len(queue1):
        # print(f'q1: {q1} s1: {s1} q2: {q2} s2: {s2}')
        if s1 == x:
            return op
        # 큐의 합 > x -> 빼야됨
        elif s1 > x:
            m = q1.popleft()
            s1 -= m
            q2.append(m)
            s2 += m
        # 큐의 합 < x -> 추가야됨
        elif s1 < x:
            m = q2.popleft()
            s2 -= m
            q1.append(m)
            s1 += m
        op += 1
    return -1
