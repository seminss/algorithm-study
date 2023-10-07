def solution(data, col, row_begin, row_end):
    answer = 0

    # 2번
    data = sorted(data, key=lambda x: (x[col - 1], -x[0]))

    # S_i 누적
    S_i = []
    for i in range(row_begin - 1, row_end):
        s = 0
        for d in data[i]:
            s += d % (i + 1)
        S_i.append(s)

    # 결과
    answer = S_i[0]
    if len(S_i) > 1:
        for s in S_i[1:]:
            answer = answer ^ s

    return answer