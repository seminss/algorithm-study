def cal_dis(x, y):
    return (x ** 2 + y ** 2) ** (1 / 2)


# x == 0 일 때부터 x를 기준으로 몇 개씩인지 계산
def solution(k, d):
    answer = 0

    # 먼저 x == 0 일 때 몇 개가 가능한지, y 좌표가 몇까지 가능한지 계산
    max = 0
    maxCount = 1
    while max <= d:
        max += k
        maxCount += 1
    max -= k
    maxCount -= 1

    # x 에 k 를 더해가면서 x == 0, k, 2k, 3k, ...  일 때 각각 계산
    lastY = max
    lastCount = maxCount
    for a in range(maxCount):
        x = k * a
        while cal_dis(x, lastY) > d:
            lastY -= k
            lastCount -= 1
        answer += lastCount

    return answer