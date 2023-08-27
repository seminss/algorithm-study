'''
H-index
https://school.programmers.co.kr/learn/courses/30/lessons/42747#
'''

def solution(citations):
    # 0부터 시작해야 한다.
    # 오답) answer = min(citations) 반례) ciations = [5,5,5]
    answer = 0 
    m = max(citations)
    h = []
    while answer <= m:
        # h 이상 인용된 논문, 이하로 인용된 논문 수
        over_h, under_h = 0, 0
        for freq in citations:
            if answer <= freq:
                over_h += 1
            elif answer >= freq:
                under_h += 1
        if answer <= over_h:
            h.append(answer)
        answer += 1
    # 빈 리스트에 대해 max 연산을 실행하면 런타임 에러 발생
    return max(h)
