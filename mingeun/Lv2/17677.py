''' 2023.5.5
13:44 ~ 14:22
'''
T = 2 # 토큰 길이
def tokenize(word: str, n: int):
    '''
    FRENCH (6, 2)
    FR RE EN NC CH
   	알파벳을 모두 소문자로 통일
    '''
    result = dict()
    for i in range(len(word)-n+1):
        token = ""
        # 알파벳인 경우만 토큰화 진행
        for j in range(n):
            if not word[i+j].isalpha():
                break
            token += word[i+j].lower()
        # 토큰의 길이가 0이면 건너뜀
        if len(token) == n:
            if token in result:
                result[token] += 1
            else:
                result[token] = 1
            
    return result

def union(d1: dict, d2: dict) -> dict:
    result = dict()
    for t in d1.keys():
        if t in d2:
            # 교집합->max(n1, n2)번 t를 추가
            result[t] = max(d1[t], d2[t])
        else:
            # d1에만 있는 원소 추가
            for i in range(d1[t]):
                result[t] = d1[t]
    # d2에만 있는 원소 추가
    for t in d2.keys():
        if t not in d1:
            result[t] = d2[t]
    return result

def intersect(d1: dict, d2: dict) -> dict:
    result = dict()
    for t in d1.keys():
        if t in d2:
            result[t] = min(d1[t], d2[t])
    return result
    

def jaccard(s1: str, s2: str):
    '''
    s1 = "aaabbcd"
    s2 = "aabeg"
    union = a a b b c d e g
    intersection = a a b 
    '''
    d1, d2 = tokenize(s1, T), tokenize(s2, T)
    _union, inter = union(d1, d2), intersect(d1, d2)
    if len(_union) == 0:
        return 1
    print(_union)
    print(inter)
    return sum(inter.values())/sum(_union.values())
    
def solution(str1, str2):
    '''
    Jaccard distance = 교집합/합집합
    * A, B가 공집합인 경우 거리는 1이 된다.
    '''
    return int(jaccard(str1, str2)*65536)
