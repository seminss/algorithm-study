from itertools import combinations
from collections import defaultdict

print(len(list(
    combinations([200, 200, 300, 300, 300], 2))))  # 10 = 2*3(2개 * 3개) + 1(200 안에서 조합 개수) + 3(300안에서 조합 개수) 임을 이용


def solution(weights):
    answer = 0

    # 먼저 중복 몸무게를 줄임
    weightCounts = defaultdict(int)
    for w in weights:
        weightCounts[w] += 1

    weights = list(weightCounts.keys())

    torque = dict()
    for i in range(len(weights)):
        for length in range(2, 5):
            tor = weights[i] * length
            if torque.get(tor, -1) == -1:
                torque[tor] = [i]
            else:
                torque[tor].append(i)

    # 먼저 torque 에서 2개 이상이 겹친 그룹의 개수끼리 곱함
    for value in torque.values():
        if len(value) < 2:
            continue
        pairs = list(combinations(value, 2))
        for a, b in pairs:
            answer += weightCounts[weights[a]] * weightCounts[weights[b]]

    # weightCounts에서 2개 이상인 것들의 조합 개수를 더함
    for count in weightCounts.values():
        if count > 1:
            answer += count * (count - 1) // 2

    return answer