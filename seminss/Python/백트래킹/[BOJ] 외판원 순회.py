import sys


def back(i,visited):
    global answer, start
    if len(cost) == n and all(visited):
        if sum(cost) < answer:
            answer = sum(cost)
        return
    for j in range(n):
        if j == i or visited[j] or maps[i][j]==0:
            continue
        if j==start and len(cost)!=n-1:
            continue
        cost.append(maps[i][j])
        visited[j]=True
        back(j,visited)
        cost.pop()
        visited[j]=False


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    maps = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    cost = []
    answer = float('inf')

    for i in range(n):
        visited=[False]*n
        start=i
        back(i,visited)

    print(answer)
