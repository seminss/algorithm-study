import sys
from collections import deque

input = sys.stdin.readline

# 국경 정사각형
# L <= 국경선 공유하는 두 나라의 인구차이 <= R 
# -> 국경선 OPEN
# 모두열려 -> 연합
# 연합을 이루고 있는 각 칸의 인구수 // 연합을 이루고 있는 칸의 개수
# 연합 해체 후 국경선 닫기
# 결과 : 인구이동 몇일 동안 발생 ?

N, L, R = map(int,input().split())
A = []
answer = 0 

for _ in range(N) :
    A.append(list(map(int,input().split())))

# 국경선 확인
dx = [0,0,1,-1]
dy = [1,-1,0,0]
union = []

def BFS(x,y) :
    queue = deque()
    queue.append([x,y])
    union = [[x,y]]

    while queue :
        pop_x, pop_y = queue.popleft()

        for i in range(4) :
            xx = pop_x + dx[i]
            yy = pop_y + dy[i]

            if 0<=xx<N and 0<=yy<N and visited[xx][yy] == False :
                if L <= abs(A[pop_x][pop_y]-A[xx][yy]) <= R :
                    visited[xx][yy] = True
                    queue.append([xx,yy])
                    union.append([xx,yy])

    return union

while True : # 계속 연합국가 있는지 확인
    visited = [[False]*N for _ in range(N)]
    moving = False

    for i in range(N) :
        for j in range(N) :
            value = 0 

            if not visited[i][j] :
                visited[i][j] = True
                union = BFS(i,j)

            if len(union) > 1 :
                moving = True # 인구이동 시작 
                for x,y in union :
                    value += A[x][y]

                for x,y in union :
                    A[x][y] = value//len(union)
    
    if not moving : # 인구이동이 없다면
        print(answer)
        break

    answer += 1
