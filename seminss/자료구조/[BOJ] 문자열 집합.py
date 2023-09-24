#10:50~10:55
import sys
n,m=map(int, sys.stdin.readline().split())
sset=[]
result=0
for i in range(n):
    sset.append(sys.stdin.readline().strip())
for j in range(m):
    str=sys.stdin.readline().strip()
    if str in sset:
        result+=1
print(result)