def solution(n):
    answer = [[]]

    towers = [[i for i in range(n, 0, -1)], [], []]
    print(towers)

    return hanoi(towers, 0, 2)


def hanoi(towers, fromNum, toNum):
    if len(towers[fromNum]) == 1:
        return [[fromNum + 1, toNum + 1]]

    if (fromNum == 0 and toNum == 1) or (fromNum == 1 and toNum == 0):
        another = 2
    else:
        another = abs(toNum - fromNum) - 1

    result = []

    recurTowers = [[], [], []]
    recurTowers[fromNum] = towers[fromNum][1:]

    result.extend(hanoi(recurTowers, fromNum, another))

    result.append([fromNum + 1, toNum + 1])

    recurTowers = [[], [], []]
    recurTowers[another] = towers[fromNum][1:]

    result.extend(hanoi(recurTowers, another, toNum))

    # 원하는 상태를 만들기 위해 옮겨야하는 타워 번호
    return result