# queue: FIFO
# 12:40~1:00
from collections import deque
def solution(priorities, location):
    answer = []
    dq=deque([chr(ord('A')+i) for i in range(len(priorities))])
    pr=deque(priorities)
    target=dq[location]
    while pr:
        mx=max(pr)
        tmp=pr.popleft()
        if tmp==mx:
            answer.append(dq.popleft())
        else:
            pr.append(tmp)
            dq.append(dq.popleft())
    return answer.index(target)+1