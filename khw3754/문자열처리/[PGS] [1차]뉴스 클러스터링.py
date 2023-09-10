from collections import defaultdict


# 2글자씩 끊은 딕셔너리로 저장
def solution(str1, str2):
    dict1, dict2 = defaultdict(int), defaultdict(int)
    # 각 문자열을 다중 집합으로 만듦
    for i in range(len(str1) - 1):
        if str1[i:i + 2].isalpha():
            dict1[str1[i:i + 2].lower()] += 1
    for i in range(len(str2) - 1):
        if str2[i:i + 2].isalpha():
            dict2[str2[i:i + 2].lower()] += 1

    # 합, 교 집합을 구함
    union, inter = {}, {}
    keys = list(dict1.keys())
    keys.extend(dict2.keys())
    keys = list(set(keys))

    for key in keys:
        union[key] = max(dict1.get(key, -1), dict2.get(key, -1))
    for key in dict1.keys():
        if dict2.get(key, -1) != -1:
            inter[key] = min(dict1[key], dict2[key])

    if sum(union.values()) == 0:
        return 65536
    else:
        return int(sum(inter.values()) / sum(union.values()) * 65536)