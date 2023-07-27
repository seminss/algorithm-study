'''2023.7.27
16:05 ~ 16:47
'''
PERSON, TABLE, PARTITION = 'P', 'O', 'X'
ROOM_SIZE = 5
from collections import deque


# BFS
def check_compliance_of_person(room, i, j):
    dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]
    visited = [[False] * ROOM_SIZE for _ in range(ROOM_SIZE)]
    visited[i][j] = True
    q = deque([[(i, j), 0]]) # 원소: (x, y), 거리
    while q:
        p, d = q.popleft()
        x, y = p[0], p[1]
        for k in range(4):
            xn, yn = x + dx[k], y + dy[k]
            if 0 <= xn < ROOM_SIZE and 0 <= yn < ROOM_SIZE \
            and not visited[xn][yn]:
                # 거리가 2이하
                if d+1 <= 2 and room[xn][yn] == PERSON:
                    # 중간에 파티션이 있다면 허용
                    if room[x][y] == PARTITION:
                        pass
                    # 중간에 파티션이 없었다면 0 반환
                    else:
                        return 0
                q.append([(xn, yn), d+1])
                visited[xn][yn] = True
    return 1


def check_compliance_of_room(room:list) -> int:
    for i in range(ROOM_SIZE):
        for j in range(ROOM_SIZE):
            # 한 명이라도 지키지 않았다면 0 반환
            if room[i][j] == PERSON and check_compliance_of_person(room, i, j) == 0:
                return 0
    # 모두 지킨 경우 1 반환
    return 1
                            

def solution(places):
    answer = []
    for room in places:
        answer.append(check_compliance_of_room(room))   
    return answer
