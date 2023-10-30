import sys
from collections import defaultdict
N,d,k,c=map(int,sys.stdin.readline().split())
data=[int(sys.stdin.readline()) for _ in range(N)]
data+=data[:k]
left,right=0,k
result=0
dict=defaultdict(int)
dict[c]+=1 #쿠폰은 일단 있다고 가정

for i in data[left:right]:
    dict[i]+=1

while right<len(data):
    result=max(result,len(dict))
    dict[data[left]]-=1 # 중복이였던 경우에는 1개 이상이 남고, 애초에 하나였던 건 지워짐
    dict[data[right]]+=1
    if dict[data[left]]==0:
        del dict[data[left]] # 해당 초밥을 못먹게 되면 dict에서 삭제
    left+=1
    right+=1
    
print(result)

# list나 deque로는 죽어도 안된다
# 중복 처리할 때 dictionary가 생각보다 편하다