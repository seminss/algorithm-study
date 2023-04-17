# n의 약수들의 튜플 리스트를 반환
def find(n):
    result = []
    for i in range(1, int(n ** (1 / 2)) + 1):
        if n % i == 0:
            result.append((i, n // i))
    return result


def solution(brown, yellow):
    answer = []

    # yellow의 약수들을 반복하며 brown의 개수와 비교
    for x, y in find(yellow):
        if 4 + x * 2 + y * 2 == brown:
            answer = [x + 2, y + 2] if x >= y else [y + 2, x + 2]
            break

    return answer