'''2023.8.12
13:50 ~ 14:19
'''

import sys


def next_index(s, ropes):
    next_start_index = s
    # skip skipduplicates
    while next_start_index < len(ropes) \
            and ropes[s] == ropes[next_start_index]:
        next_start_index += 1
    if next_start_index == s:
        next_start_index += 1
    return next_start_index


def solution():
    n = int(sys.stdin.readline())
    ropes = [int(input()) for _ in range(n)]
    ropes.sort()
    answer = 0
    rope_index = 0
    while rope_index < n:
        rope_count = n - rope_index
        answer = max(answer, rope_count * ropes[rope_index])
        rope_index = next_index(rope_index, ropes)
    print(answer)


def faster_solution():
    """
    인덱스가 밧줄이 견디는 최대 무게이고
    값이 해당 밧줄의 개수인 배열을 사용한다.
    """
    n = int(sys.stdin.readline())
    rope_count = [0] * 10001

    # 각 로프의 개수 저장
    for _ in range(n):
        rope_count[int(input())] += 1

    answer, capacity, total_rope_count = 0, 0, 0
    for w in range(10000, -1, -1):
        # 견딜 수 있는 무게가 w인 이상인 밧줄의 개수
        total_rope_count += rope_count[w]
        capacity = total_rope_count * w
        answer = max(answer, capacity)

    print(answer)


solution()

# faster_solution()
