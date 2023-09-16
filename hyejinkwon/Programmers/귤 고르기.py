'''
def solution(k, tangerine):
    answer = 0
    orange = {}
    for t in tangerine :
        if t in orange :
            orange[t] += 1
        else :
            orange[t] = 1
            
    orange = sorted(orange.items(), key = lambda x :x[1], reverse=True)
    
    for o_key, o_value in orange : 
        k -= o_value
        answer += 1
        if k <= 0 :
            break
    
    return answer
'''

# Counter 사용
import collections

def solution(k, tangerine):
    answer = 0
    kind = collections.Counter(tangerine)
    kind = sorted(kind.values(), reverse=True)
    
    for value in kind :
        answer += 1
        k -= value
        if k <=0 :
            break
            
    return answer