'''2023.8.13
10:04 ~ 10:15
'''
import sys
import heapq
input = sys.stdin.readline


def solution():
    n = int(input())
    START, END = 0, 1
    meetings = [list(map(int, input().split(' '))) for _ in range(n)]
    meetings.sort(key=lambda x: x[0])
    meetings_in_progress = []
    answer = 0
    for meeting in meetings:
        # 새로운 회의실 필요
        if len(meetings_in_progress) == 0\
                or meetings_in_progress[0] > meeting[START]:
            answer += 1
            heapq.heappush(meetings_in_progress, meeting[END])
        # 진행중인 회의가 끝나서 새로운 회의실이 필요 없음
        elif len(meetings_in_progress) > 0\
                and meetings_in_progress[0] <= meeting[START]:
            heapq.heappop(meetings_in_progress)
            heapq.heappush(meetings_in_progress, meeting[END])
    print(answer)


solution()
