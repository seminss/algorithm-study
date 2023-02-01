import sys
N,M=map(int,sys.stdin.readline().split())

pwd_list={}

for i in range(N):
    adr,pwd=map(str,sys.stdin.readline().split())
    pwd_list[adr]=pwd

for j in range(M):
    search_adr=sys.stdin.readline().strip()
    print(pwd_list[search_adr])