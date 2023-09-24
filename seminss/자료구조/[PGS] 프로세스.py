# queue: FIFO
#12:37~
from collections import deque
def solution(priorities, location):
    answer = []
    dq = deque([(v,chr(ord('A')+i)) for i,v in enumerate(priorities)])
    target=dq[location]
    print(max(dq,key=lambda x:x[0]))
    while dq:
        mx=max(dq,key=lambda x:x[0])
        tmp=dq.popleft()
        if tmp!=mx:
            dq.append(tmp)
        else:
            answer.append(tmp)
    return answer.index(target)+1
