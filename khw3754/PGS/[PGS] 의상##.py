from collections import defaultdict

def solution(clothes):
    dict_ = defaultdict(int)
    for i, x in clothes:
        dict_[x] += 1

    vals = list(dict_.values())
    count = 1
    for i in vals:
        count *= i + 1

    return count - 1