import sys
N,K=map(int,sys.stdin.readline().split())
circle=[0 for i in range(N)]
order=[0 for i in range(N)]

for i in range(N):
    circle[i]=i+1

circle.reverse()
for w in range(N):
    for j in range(K-1):
        a=circle.pop()
        circle.insert(0,a)
    o=circle.pop()
    order[w]=o

#출력
print("<",end="")
for i in order:
    if i==order[N-1]:
        print(i,end=">")
    else:
        print(i,end=", ")