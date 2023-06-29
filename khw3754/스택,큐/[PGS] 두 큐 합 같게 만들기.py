from collections import deque


def solution(queue1, queue2):
    answer = 0

    total = sum(queue1) + sum(queue2)
    half = total // 2
    if total % 2 != 0:
        return -1
    queue1 = deque(queue1)
    queue2 = deque(queue2)

    sum1, sum2 = sum(queue1), sum(queue2)
    count1, count2 = len(queue1), len(queue2)
    while count1 > 0 or count2 > 0:
        if sum1 == sum2:
            break
        elif sum1 > half:
            tmp = queue1.popleft()
            queue2.append(tmp)
            sum1 -= tmp
            sum2 += tmp
            count1 -= 1
        elif sum2 > half:
            tmp = queue2.popleft()
            queue1.append(tmp)
            sum2 -= tmp
            sum1 += tmp
            count2 -= 1
        answer += 1

    else:
        answer = -1

    # print(queue1, sum(queue1))
    # print(queue2, sum(queue2))

    return answer