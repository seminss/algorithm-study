import sys

N = int(sys.stdin.readline())

board = [[0 for _ in range(N)] for _ in range(N)]
likeList = [[] for _ in range(N*N+1)]

# 상하좌우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for _ in range(N*N):
    like = list(map(int, sys.stdin.readline().split()))
    stuNum = like.pop(0)

    likeList[stuNum] = like

    # (1,1) 부터 모든 빈 자리를 탐색
    # 400*400*4 = 640,000 이기 때문에 완전탐색으로 다 돌아도 상관없음
    targetSeat = [-1, -1, -1 -1]   # [x, y, 좋아하는 학생 수, 인접한 칸 수]
    for y in range(N):
        for x in range(N):
            if board[y][x] != 0:
                continue
            # (x,y) 의 좋아하는 학생 수, 인접한 칸 수를 조사
            likeCount = 0
            emptyCount = 0
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < N and 0 <= ny < N:
                    if board[ny][nx] == 0:
                        emptyCount += 1
                    elif board[ny][nx] in like:
                        likeCount += 1

            # 현재 자리보다 우선순위가 높다면 교체
            if targetSeat[2] < likeCount or (targetSeat[2] == likeCount and targetSeat[3] < emptyCount):
                targetSeat = [x, y, likeCount, emptyCount]

    # 해당 자리로 학생을 넣음 (학생 번호, 좋아하는 학생 수)
    board[targetSeat[1]][targetSeat[0]] = stuNum

print(board)

# 학생의 만족도를 구함
result = 0
for y in range(N):
    for x in range(N):
        stuNum = board[y][x]
        likeCount = 0
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and board[ny][nx] in likeList[stuNum]:
                likeCount += 1

        if likeCount != 0:
            result += 10**(likeCount-1)

print(result)