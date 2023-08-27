from itertools import combinations as combi
from collections import defaultdict


def solution(orders, course):
    answer = []

    counter = defaultdict(int)

    for order in orders:
        for c in course:
            for target in list(map(lambda x: ''.join(sorted(x)), list(combi(order, c)))):
                counter[target] += 1

    counter = dict(filter(lambda x: x[1] > 1, counter.items()))
    max_lens = {i: 0 for i in course}

    for k, v in counter.items():
        if max_lens[len(k)] < v:
            max_lens[len(k)] = v

    for k, v in counter.items():
        if v == max_lens[len(k)]:
            answer.append(k)

    return sorted(answer)