import sys

input = sys.stdin.readline
T = int(input())
for _ in range(T) :
    M,N,X,Y = map(int, input().split())

    for K in range(X, M*N+1,M) :
        if (K-X)%M ==0 and (K-Y)%N==0 : 
            print(K)
            break
    else:
        print(-1)
    