# 각 원소의 합 s + 원소의 곱이 최대

def solution(n, s):
    answer = []
    combi = []
    
    if n > s : return [-1]

    for i in range(n) :
        combi.append(s//n) 
        
    if s%n != 0 :
        for i in range(1,s%n+1) :
            combi[n-i] += 1
            
    answer = combi
    
    return answer