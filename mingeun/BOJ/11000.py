'''2023.8.12
16:38 ~ 17:17
'''
from heapq import heappop, heappush
import sys


def solution():
    # n <= 2 * 10^5
    n = int(sys.stdin.readline())
    lectures = [list(map(int, sys.stdin.readline().split(' '))) for _ in range(n)]
    lectures.sort(key=lambda x: (x[0], x[1]))
    answer = 0
    # 최대 n개의 강의실이 필요하다.
    # 강의가 끝나는 시각 목록
    START, END = 0, 1
    end_times = []
    for i in range(n):
        # 강의실을 추가하는 경우
        if len(end_times) == 0 or end_times[0] > lectures[i][START]:
            answer += 1
            heappush(end_times, lectures[i][END])
        # 강의실을 추가할 필요가 없는 경우
        elif len(end_times) > 0 and end_times[0] <= lectures[i][START]:
            heappush(end_times, lectures[i][END])
            heappop(end_times)
    print(answer)


solution()
