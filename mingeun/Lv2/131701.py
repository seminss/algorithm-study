# 연속 부분 수열의 합 개수 
# https://school.programmers.co.kr/learn/courses/30/lessons/131701
# 2023.5.2 18:07 ~ 18:27
def solution(elements):
    n = len(elements)
    # 연속된 j개를 더하여 results에 기록
    results = set([])
    # i가 포함된 모든 연속된 수열합 계산
    for i in range(n):
        for j in range(1, n+1):
            # 순환
            if i+j >= n:
                _sum = sum(elements[i:]) + sum(elements[:(i+j)%n])
            # 직선
            else:
                _sum = sum(elements[i:i+j])
            results.add(_sum)
    return len(results)
