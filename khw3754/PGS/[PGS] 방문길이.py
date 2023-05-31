'''
지나간 길을 가지고 있어야 한다.
가로/세로로 이동한 것을 가지고있는 딕셔너리로 저장
wdict = {x좌표: [(작은y, 큰y)]}
hdict = {y좌표: [(작은x, 큰x)]}
'''


def check(x, y):
    if -5 <= x <= 5 and -5 <= y <= 5:
        return True
    else:
        return False


def solution(dirs):
    answer = 0

    wdict = {i: [] for i in range(-5, 6)}
    hdict = {i: [] for i in range(-5, 6)}

    pos = [0, 0]
    for dir in dirs:
        if dir == 'L':
            # 경계 안이고
            if check(pos[0], pos[1] - 1):
                # 지나간 적이 없는 길이면
                if (pos[1] - 1, pos[1]) not in wdict[pos[0]]:
                    wdict[pos[0]].append((pos[1] - 1, pos[1]))
                    answer += 1  # count
                pos[1] -= 1
        if dir == 'R':
            # 경계 안이고
            if check(pos[0], pos[1] + 1):
                # 지나간 적이 없는 길이면
                if (pos[1], pos[1] + 1) not in wdict[pos[0]]:
                    wdict[pos[0]].append((pos[1], pos[1] + 1))
                    answer += 1  # count
                pos[1] += 1
        if dir == 'D':
            # 경계 안이고
            if check(pos[0] - 1, pos[1]):
                # 지나간 적이 없는 길이면
                if (pos[0] - 1, pos[0]) not in hdict[pos[1]]:
                    hdict[pos[1]].append((pos[0] - 1, pos[0]))
                    answer += 1  # count
                pos[0] -= 1
        if dir == 'U':
            # 경계 안이고
            if check(pos[0] + 1, pos[1]):
                # 지나간 적이 없는 길이면
                if (pos[0], pos[0] + 1) not in hdict[pos[1]]:
                    hdict[pos[1]].append((pos[0], pos[0] + 1))
                    answer += 1  # count
                pos[0] += 1

    return answer