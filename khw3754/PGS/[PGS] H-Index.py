def solution(citations):
    citations = sorted(citations)
    m = 0
    for i in range(1, len(citations) + 1):
        if citations[-1 * i] >= i:
            m = i
        else:
            break

    return m