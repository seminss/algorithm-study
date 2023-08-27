# 약수들을 구해주는 함수
def divisors(num):
    result = [num]
    for i in range(2, int(num ** (1 / 2)) + 1):
        if num % i == 0:
            result.append(i)
            if i * i != num:
                result.append(num // i)
    return sorted(result)


def solution(arrayA, arrayB):
    answer = 0

    for _arrayA, _arrayB in [(arrayA, arrayB), (arrayB, arrayA)]:
        # A와 B 중 한 사람의 카드를 모두 나눌 수 있는 수들을 구함
        # 최소값의 약수들 (1 제외)
        divs = divisors(min(_arrayA))

        # 최소값의 약수 중 나의 카드를 모두 나눌 수 있는 수들을 가져옴
        targets = []
        for d in divs:
            for a in _arrayA:
                if a % d != 0:
                    break
            else:
                targets.append(d)

        # 약수들 중에서 가장 큰 값부터 상대의 카드의 수를 나눌 수 있는 지 검사
        for target in targets[::-1]:
            if len(list(filter(lambda x: x % target == 0, _arrayB))) == 0 and answer < target:
                answer = target
                break

    return answer