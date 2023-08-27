''' 2023.5.4
19:53 ~ 20:10
'''
from collections import deque
def solution(progresses, speeds):
    answer = []
    progresses = deque(progresses)
    # speeds 도 큐로 만들어서 길이가 progresses와 같도록 유지해줘야된다.
    speeds = deque(speeds)
    while progresses:
        print(progresses)
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        # 맨 앞에 완성된 기능이 있는 경우
        if progresses[0] >= 100:
            complete = 0
            # progresses의 길이가 0일 수도 있다.
            while len(progresses) > 0 and progresses[0] >= 100:
                progresses.popleft()
                speeds.popleft()
                complete += 1
            answer.append(complete)
    return answer
