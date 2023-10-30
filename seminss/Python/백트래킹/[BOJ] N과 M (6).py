import sys

N, M = map(int, sys.stdin.readline().split())
data = sorted(list(map(int, sys.stdin.readline().strip().split())))
temp = []


def back(start):
    if len(temp) == M:
        print(*temp)
        return

    for i in range(start, N):
        if data[i] not in temp:
            temp.append(data[i])
            back(i + 1)
            temp.pop()


back(0)
