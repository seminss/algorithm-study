import sys
N=int(sys.stdin.readline())
location=[0 for i in range(N)]

for i in range(N) :
    location[i]=tuple(map(int,sys.stdin.readline().split()))

location.sort()
for x,y in location:
    print(x,y)