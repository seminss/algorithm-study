N, K = map(int, input().split())
si = list(map(int, input().split()))
di = list(map(int, input().split()))

for _ in range(K):
    tmp = [0] * N
    for i in range(N):
        tmp[di[i]-1] = si[i]
    si = tmp

print(*si)