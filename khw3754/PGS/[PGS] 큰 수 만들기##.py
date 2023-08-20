def find(num):
    m = num[0]
    idx = 0

    for i, n in enumerate(num):
        if int(m) < int(n):
            m = n
            idx = i
        if m == '9':
            return idx, m

    return idx, m


def solution(number, k):
    answer = ''

    i = len(number) - k
    tmp = i
    # 맨 앞자리 수부터 하나씩 고름
    for _ in range(tmp):
        if i == 1:
            answer += max(number[::])
            break

        index, m = find(number[:-i + 1])
        # m = max(number[:-i+1])
        # index = number[:-i+1].index(m)

        answer += m
        number = number[index + 1:]
        i -= 1

    return answer