'''2023.8.20
-1
'''
import sys

input = sys.stdin.readline


def enough_time(time, n, m, required_times):
    """
    각 심사대에서 심사받을 수 있는 사람의 수가
    m보다 크면 가능
    """
    capacity = 0
    for i in range(n):
        capacity += time // required_times[i]
    return capacity >= m


def bin_search(n, m, required_times):
    """
    이분 탐색을 통해 n개의 심사대가 m명의 사람을
    심사하는데 걸리는 최소 시간을 찾는다.
    범위: 1 * m <= answer <= 10^9 * m
    log2(10^20) ~ 66
    """
    left, right = min(required_times), max(required_times) * m
    x = right
    while left <= right:
        mid = (left + right) // 2
        if enough_time(mid, n, m, required_times):
            right = mid - 1
            x = min(x, mid)
        else:
            left = mid + 1
    return x


def solution():
    n, m = map(int, input().split(' '))
    required_times = [int(input()) for _ in range(n)]

    print(bin_search(n, m, required_times))


solution()
