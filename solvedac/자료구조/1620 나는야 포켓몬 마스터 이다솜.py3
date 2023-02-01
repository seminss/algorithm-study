import sys

n,m=map(int,sys.stdin.readline().split())

poketmon={}

for i in range(n):
    poketmon[i+1]=sys.stdin.readline().strip()
re_poketmon= dict(map(reversed,poketmon.items()))

for j in range(m):
    q=sys.stdin.readline().strip()
    if q.isdigit():
        print(poketmon[int(q)])
    else:
        print(re_poketmon[q])