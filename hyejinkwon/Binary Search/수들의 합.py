import sys

input = sys.stdin.readline

S = int(input())
n = 1
# 1부터 n 까지의 합 공식 : n*(n+1)//2

while n*(n+1)//2 <= S :
    n += 1

print(n-1) 