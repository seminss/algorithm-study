import sys
T=int(sys.stdin.readline())

#C(M,N): M개 중에 N개를 선택하는 경우의 수
#조합 공식: M!/(M-N)!N!

for _ in range(T):
    N,M=map(int,sys.stdin.readline().split())
    facto=[0]*(M+1)
    facto[0]=1
    
    for i in range(1,M+1):
        facto[i]=facto[i-1]*i

    print(int(facto[M]/(facto[M-N]*facto[N])))