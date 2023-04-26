import sys
from collections import deque

input = sys.stdin.readline

M,N = map(int,input().split())
box = []
queue = deque([])

# 주변 바로바로 탐색 BFS 이용
# 1 : 익은 토마토 
# 0 : 익지 않은 토마토 
# -1 : 없는 토마토

for i in range(N) :
    tomato = list(map(int,input().split()))
    box.append(tomato)

for i in range(N) :
    for j in range(M) :
        if box[i][j] == 1 : # 익은 토마토 발견
            queue.append([i,j])

if len(queue) == N*M : #모두 다 익은 상황
    print(0)
    exit(0)

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def BFS() :
    global day
    while queue :
        x,y = queue.popleft()

        for k in range(4) :
            xx = x + dx[k]
            yy = y + dy[k]

            if 0<=xx<=N-1 and 0<=yy<=M-1 and box[xx][yy] == 0 :
                queue.append([xx,yy])
                box[xx][yy] = box[x][y] + 1 # 익어버림

BFS()
day = 0
for row_box in box :
    for j in row_box :
        if j == 0 : # 하나라도 익지 않았다면 
            print(-1)
            exit(0)
    day = max(day, max(row_box))

print(day)
