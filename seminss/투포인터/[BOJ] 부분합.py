#2:06~2:12
import sys
from collections import deque
n,m=map(int,sys.stdin.readline().split())
A=deque(map(int,sys.stdin.readline().split()))
B=deque(map(int,sys.stdin.readline().split()))
arr=[]
while A and B:
    if A[0]<B[0]:
        arr.append(A.popleft())
    else:
        arr.append(B.popleft())
arr=arr+list(A)+list(B)
print(*arr)

#그냥 sort해서 join 해도 되는 문젠데 어렵게 생각했다..