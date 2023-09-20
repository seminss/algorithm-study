import sys
input = sys.stdin.readline

N,M = map(int,input().split())
L = list(map(int, input().split()))
prefix = [0]
value = 0
for i in range(N) :
    value += L[i]
    prefix.append(value)

for _ in range(M) :
    s,e = map(int,input().split())
    print(prefix[e-1] - prefix[s-1])