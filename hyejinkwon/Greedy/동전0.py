import sys

input = sys.stdin.readline
N, K = map(int, input().split())
coin = []
answer = 0 

for _ in range(N) :
    coin.append(int(input()))

for i in range(N-1,-1,-1):
    answer += K//coin[i]
    K %= coin[i]

print(answer)