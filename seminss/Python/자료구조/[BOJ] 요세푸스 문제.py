import sys
from collections import deque
n,k=map(int,sys.stdin.readline().split())
queue=deque([i for i in range(1,n+1)])

cnt=0
print("<",end="")
while cnt!=n-1:
    for i in range(k-1):
        queue.append(queue.popleft())
    cnt+=1
    print(queue.popleft(),end=", ")
print("{0}>".format(queue.popleft()))