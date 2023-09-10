from collections import deque

'''
큐에 담아놓고 매일 speeds를 각각 더해주고 
맨 앞 일이 100%가 되면 앞에서부터 100%인거 쭉 빼기
'''


def solution(progresses, speeds):
    answer = []

    progresses = deque(progresses)
    speeds = deque(speeds)
    while progresses:
        # 모두 진도율 +
        for i in range(len(speeds)):
            progresses[i] += speeds[i]
        # 앞에서 부터 진도율이 100% 이상인 것들을 pop
        count = 0
        while progresses and progresses[0] >= 100:
            progresses.popleft()
            speeds.popleft()
            count += 1
        if count > 0:
            answer.append(count)

    return answer