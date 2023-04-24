# 귤 고르기
# https://school.programmers.co.kr/learn/courses/30/lessons/138476

def solution(k, tangerine):
    """
    {종류(무게): 개수} 딕셔너리를 초기화한다.
    개수를 기준으로 종류를 내림차순으로 정렬하기 위해 [[종류, 개수]] 리스트를 초기화한다.
    k가 0보다 작아질때까지 개수가 많은 순서대로 그 개수를 k에서 빼준다. 뺄 때마다 answer += 1.
    """
    kind = dict()
    for t in tangerine:
        if t in kind:
            kind[t] += 1
        else:
            kind[t] = 1
    # [크기, 개수]
    tmp = [[k, v] for k,v in kind.items()]
    tmp.sort(reverse=True, key=lambda x:x[1])
    i = 0
    answer = 0
    while k > 0:
        # i번째로 개수가 많은 귤 종류 tmp[i][1]
        k = k - tmp[i][1]
        i += 1
        answer += 1
    return answer
