from collections import deque


def solution(prices):
    answer = []
    prices = deque(prices)

    while prices:
        target = prices.popleft()

        count = 1
        for price in prices:
            if target > price:
                answer.append(count)
                break
            count += 1
        else:
            answer.append(count - 1)

    return answer