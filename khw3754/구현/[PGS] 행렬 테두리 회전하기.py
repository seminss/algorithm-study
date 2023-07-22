def solution(rows, columns, queries):
    answer = []

    map = [[j + i * columns for j in range(1, columns + 1)] for i in range(0, rows)]

    for x1, y1, x2, y2 in queries:
        x1 -= 1
        y1 -= 1
        x2 -= 1
        y2 -= 1

        # 라인 식별
        line = []
        for y in range(y1, y2 + 1):
            line.append(map[x1][y])
        for x in range(x1 + 1, x2 + 1):
            line.append(map[x][y2])
        for y in range(y2 - 1, y1 - 1, -1):
            line.append(map[x2][y])
        for x in range(x2 - 1, x1, -1):
            line.append(map[x][y1])

        # 라인 돌리기
        line = [line[-1]] + line[:-1]

        # 가장 작은 수 추가
        answer.append(min(line))

        # 라인 적용
        idx = 0
        for y in range(y1, y2 + 1):
            map[x1][y] = line[idx]
            idx += 1
        for x in range(x1 + 1, x2 + 1):
            map[x][y2] = line[idx]
            idx += 1
        for y in range(y2 - 1, y1 - 1, -1):
            map[x2][y] = line[idx]
            idx += 1
        for x in range(x2 - 1, x1, -1):
            map[x][y1] = line[idx]
            idx += 1

    return answer