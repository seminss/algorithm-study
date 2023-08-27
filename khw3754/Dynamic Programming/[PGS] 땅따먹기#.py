def solution(land):
    for i in range(1, len(land)):
        for j in range(4):
            targets = []
            targets.extend(land[i - 1][:j])
            targets.extend(land[i - 1][j + 1:])
            land[i][j] += max(targets)

    return max(land[-1])