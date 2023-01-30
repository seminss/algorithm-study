import sys
N=int(sys.stdin.readline())
location=[0 for i in range(N)]

for i in range(N) :
    x,y=map(int,sys.stdin.readline().split())
    location[i]=(y,x)

location.sort()
for y,x in location:
    print(x,y)