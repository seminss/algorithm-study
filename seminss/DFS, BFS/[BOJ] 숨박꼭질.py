import sys
from collections import deque

inf = 100000
n, k = map(int, sys.stdin.readline().split())
q = deque([n])
tmp = [0] * (inf + 1)  # 이동 횟수를 저장하기 위한 배열

while q:
    t = q.popleft()
    if t == k:
        print(tmp[t])
        break
    for i in (t - 1, t + 1, t * 2):
        if inf >= i >= 0 == tmp[i]:  # 방문한 곳은 방문 하지 않음
            tmp[i] = tmp[t] + 1
            q.append(i)

# 최단 경로를 어떻게 찾아야 고민을 했는데, 인덱스에 누적 카운트를 해야 하는 방식이었다.
# bfs지만 메모리 초과를 고려하기 위해 방문했던 곳은 방문하지 않도록 처리했다.
# dfs를 사용하지 depth를 초과했던건지, 런타임 에러가 났다.
