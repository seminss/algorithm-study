# 사람을 기준으로 주변 검사하는 함수(지켜지고 있으면 True, 아니면 False)
def check_around(room, x, y):
    # 상하좌우 검사
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if not (0 <= nx < 5 and 0 <= ny < 5):
            continue
        if room[ny][nx] == 'P':
            return False
        elif room[ny][nx] == 'O':
            checkList = [(nx + dx[i], ny + dy[i]), (nx + dy[i], ny + dx[i]), (nx - dy[i], ny - dx[i])]
            for tx, ty in checkList:
                if 0 <= tx < 5 and 0 <= ty < 5 and room[ty][tx] == 'P':
                    return False

    return True


# 대기실을 확인하는 함수
def room_check(room):
    # 사람이 있으면 그 사람을 기준으로 검사
    for y in range(len(room)):
        line = room[y]
        for x in range(len(line)):
            seet = line[x]
            if seet == 'P':
                if not check_around(room, x, y):
                    return 0

    return 1


def solution(places):
    answer = []

    for room in places:
        answer.append(room_check(room))

    return answer