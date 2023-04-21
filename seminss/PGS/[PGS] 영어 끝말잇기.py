import math
def solution(n, words):
    answer = [0,0]
    last=words[0][-1]
    before=[words[0]]
    for i,w in enumerate(words[1:]):
        if len(w)==1 or w[0]!=last or w in before:
            answer[0]=(i+1)%n+1
            answer[1]=math.ceil((i+2)/n)
            break
        before.append(w)
        last=w[-1] #마지막 단어 저장
    return answer