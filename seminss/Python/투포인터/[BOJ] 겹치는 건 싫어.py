# dic에 +1씩 해서 k개 보다 큰 게 있으면 out
#11:20~
import sys
from collections import defaultdict

n,k=map(int,sys.stdin.readline().split())
data=list(map(int,sys.stdin.readline().split()))
dict=defaultdict(int)

head=0
tail=0
max_cnt=0

while head<n:
    if dict[data[head]]<k:
        dict[data[head]]+=1
        head+=1
    else:
        dict[data[tail]]-=1
        tail+=1
    max_cnt=max(max_cnt,head-tail)

print(max_cnt)