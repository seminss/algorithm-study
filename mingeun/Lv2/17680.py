'''
[1차] 캐시
https://school.programmers.co.kr/learn/courses/30/lessons/17680
'''
from collections import deque
def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5
    answer = 0
    # cache 초기화
    cset = set()
    cque = deque()
    for city in cities:
        c = city.lower()
        # miss
        if c not in cset:
            # cache가 꽉 참
            if len(cset) == cacheSize:
                cset.remove(cque.popleft())
            cset.add(c)
            cque.append(c)
            answer += 5
        # hit
        else:
            if len(cque) > 0:
                cque.remove(c)
                cque.append(c)
            answer += 1
    return answer

