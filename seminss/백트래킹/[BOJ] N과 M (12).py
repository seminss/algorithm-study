import sys

N, M = map(int, sys.stdin.readline().split())
data = sorted(list(set(map(int, sys.stdin.readline().strip().split()))))
ans = []


def back(start):
    if len(ans) == M:
        print(*ans)
        return
    for i in range(start, len(data)):
        ans.append(data[i])
        back(i)
        ans.pop()


back(0)
