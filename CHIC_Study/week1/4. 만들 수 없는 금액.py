#만들 수 없는 금액
import sys
n=int(sys.stdin.readline())
data=list(map(int,sys.stdin.readline().split()))

data.sort()
num=1

for i in data:
    if num<i:
        break
    num+=i
print(num)