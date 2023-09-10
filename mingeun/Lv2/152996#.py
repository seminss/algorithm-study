'''2023.08.07
-1
'''
from math import factorial
from collections import Counter


def nCr(n, r):
    r = min(r, n-r)
    return factorial(n)//(factorial(n-r)*factorial(r))

    
def solution(weights):
    answer = 0
    counter = Counter(weights)
    # 몸무게 비율이 1:1
    for w in counter:
        if counter[w] > 1:
            answer += nCr(counter[w], 2)
    # 몸무게 비율이 2:3, 2:4, 3:4
    for w in counter:
        if w*2/3 in counter:
            answer += counter[w] * counter[w*2/3]
        if w*2 in counter:
            answer += counter[w] * counter[w*2]
        if w*3/4 in counter:
            answer += counter[w] * counter[w*3/4]
    return answer
