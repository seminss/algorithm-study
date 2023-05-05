from collections import deque


def solution(pris, location):
    answer = 1

    pris = deque(pris)
    while pris:
        # 실행 1
        task = pris.popleft()

        # 에외처리: 마지막 task인 경우
        if not pris:
            return answer

        # 실행 2
        if max(pris) > task:
            pris.append(task)
        # 실행 3
        else:
            if location == 0:
                return answer
            else:
                answer += 1
        # 위치 동기화
        location -= 1
        if location < 0:
            location = len(pris) - 1

    return answer