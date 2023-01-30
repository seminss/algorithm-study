import sys
m,n = map(int,sys.stdin.readline().split())

for e in range(m,n+1):
    prime=1
    for j in range(2,int(e**0.5)+1):
        if e%j==0:
            prime=0
            break
    if prime==1 and e!=1:
        print(e)