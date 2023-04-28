import sys
input = sys.stdin.readline

N,M = map(int, input().split())
A_LIST = list(map(int, input().split()))
B_LIST = list(map(int, input().split()))

A_LIST += B_LIST
A_LIST.sort()

answer = ' '.join(map(str, A_LIST))
print(answer)

for a in A_LIST :
    print(a,end=" ")