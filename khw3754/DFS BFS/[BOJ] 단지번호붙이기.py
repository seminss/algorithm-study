from collections import deque
# 해당 x,y 좌표에서 덩어리의 크기를 구해서 반환하는 함수
def bfs(map, visited, x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque()
    q.append((x, y))
    visited[y][x] = True
    count = 1

    while q:
        tx, ty = q.popleft()
        for i in range(4):
            nx, ny = tx + dx[i], ty + dy[i]
            if 0 <= nx < len(map) and 0 <= ny < len(map) and map[ny][nx] == '1' and not visited[ny][nx]:
                count += 1
                visited[ny][nx] = True
                q.append((nx, ny))

    return count

def main():
    N = int(input())
    map = []
    visited = [[False for _ in range(N)] for i in range(N)]
    for y in range(N):
        map.append(input())

    result = []
    for y in range(N):
        for x in range(N):
            if not visited[y][x] and map[y][x] == '1':
                result.append(bfs(map, visited, x, y))

    print(len(result))
    for i in sorted(result):
        print(i)

main()