import sys

input = sys.stdin.readline
T = int(input())
for _ in range(T) :
    N,M,X,Y = map(int, input().split())

    answer = False
    for K in range(X, M*N+1,M) :
        if (K-X)%M ==0 and (K-Y)%N==0 : 
            print(K)
            break
    else:
        print(-1)
    