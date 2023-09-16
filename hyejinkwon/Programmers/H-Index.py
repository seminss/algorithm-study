'''
def solution(citations):
    answer = 0    
    
    while answer <= max(citations) :
        ok = 0
        
        for c in citations :
            if c > answer :
                ok += 1

        if answer >= ok :
            return answer 
        else :
            answer += 1
            ok = 0
        
    return answer
'''

def solution(citations):
    answer = 0    
    citations.sort(reverse=True)
    
    for c in citations:
        if c > answer :
            answer += 1
    
    return answer