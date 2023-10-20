'''
1  1세대 Rr
4  2세대 RR           Rr           Rr           rr
16 3세대 RR RR RR RR  RR Rr Rr rr  RR Rr Rr rr  rr rr rr rr
64 4세대
'''

def how(generation, billings) :
    stack = []
    billings -= 1
    
    while generation > 1 :
        stack.append(billings%4) 
        generation -= 1
        billings //= 4
        
    while stack :
        val = stack.pop()
        if val == 0 : return "RR"
        elif val == 3 : return "rr"
    return "Rr"

def solution(queries):
    answer = []
    
    for a,b in queries :
        answer.append(how(a,b))
    
    return answer