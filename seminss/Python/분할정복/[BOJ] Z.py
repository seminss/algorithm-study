import sys

n,r,c=map(int,sys.stdin.readline().split())

def Z(n,r,c):
    if n==0:
        return 0
    return 2*(r%2)+(c%2)+4*Z(n-1,int(r/2),int(c/2))

print(Z(n,r,c))