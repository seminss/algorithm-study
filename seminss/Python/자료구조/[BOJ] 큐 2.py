import sys
from collections import deque

#popleft()
#queue=dequeu(리스트)

n=int(sys.stdin.readline())
queue=deque()

for i in range(n):
    calculation=sys.stdin.readline()
    if 'push' in calculation:
        cal,num=map(str,calculation.split())
        queue.append(int(num))
    elif 'pop' in calculation:
        if len(queue)==0:
            print(-1)
        else:
            print(queue.popleft())
    elif 'size' in calculation:
        print(len(queue))
    elif 'empty' in calculation:
        if len(queue)==0:
            print(1)
        else:
            print(0)
    elif 'front' in calculation:
        if len(queue)==0:
            print(-1)
        else:
            print(queue[0])
    elif 'back' in calculation:
        if len(queue)==0:
            print(-1)
        else:
            print(queue[-1])
