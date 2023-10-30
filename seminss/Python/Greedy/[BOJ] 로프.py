import sys

n = int(sys.stdin.readline())
ropes=[]

for _ in range(n):
    ropes.append(int(sys.stdin.readline()))

ropes.sort()
answer=0
for i,rope in enumerate(ropes):
    if rope*(n-i)>answer:
        answer=rope*(n-i)
print(answer)