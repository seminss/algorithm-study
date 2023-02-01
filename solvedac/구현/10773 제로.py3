import sys
k = int(sys.stdin.readline())
stack=[]
cnt=0
#stack FIFO:first in first out
for i in range(k):
    num=int(sys.stdin.readline())
    if num==0 and len(stack)!=0:
        stack.pop()
    else:
        stack.append(num)
for e in stack:
    cnt+=e
print(cnt)