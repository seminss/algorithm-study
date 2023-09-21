import sys

input = sys.stdin.readline
N, K = map(int, input().split())
coin = []
answer = 0 

for _ in range(N) :
    coin.append(int(input()))

coin.sort()


