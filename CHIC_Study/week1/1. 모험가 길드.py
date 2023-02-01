#01 모험가 길드
import sys
n=int(sys.stdin.readline())
list=list(map(int,sys.stdin.readline().split()))
list.sort()

result=0
cnt=0

for i in list:
    cnt+-1
    if cnt>=1:
        result+=1
        cnt=0
print(result)
    
print(cnt)