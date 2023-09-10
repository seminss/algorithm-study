'''2023.8.13
10:25 ~ 10:36
'''
import sys
input = sys.stdin.readline


def elapsed_time_for_withdrawl(queue):
    """
    1 2 3 3 4
    1 = 1
    3 = 1 + 2
    6 = 1 + 2 + 3
    9 = 1 + 2 + 3 + 3
    13 = 1 + 2 + 3 + 4
    """
    result = 0
    for i, time in enumerate(queue):
        n = len(queue)
        result += (n-i) * time
    return result


def solution():
    int(input())
    required_times = list(map(int, input().split(' ')))
    best_order = sorted(required_times)
    print(elapsed_time_for_withdrawl(best_order))


solution()
