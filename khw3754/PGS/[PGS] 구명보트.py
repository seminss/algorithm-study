from collections import deque


def solution(people, limit):
    answer = 0

    people = deque(sorted(people, reverse=True))
    while len(people) > 0:
        lim = limit
        # 가장 무거운 사람 한 명 탑승
        lim -= people.popleft()

        # 가벼운 순으로 탈 수 있을 만큼 탑승
        while people:
            if lim >= people[-1]:
                lim -= people.pop()
            else:
                break

        answer += 1

    return answer