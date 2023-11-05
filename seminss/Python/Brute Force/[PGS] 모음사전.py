from itertools import product

def solution(word):
    words=[]
    for i in range(1,6):
        for c in product(['A','E','I','O','U'],repeat=i):
            words.append(''.join(list(c)))
    words.sort()
    return words.index(word)+1

# 중복 순열 함수 product : 서로다른 n개, 중복을 허락하고 r개를 일렬로 나열