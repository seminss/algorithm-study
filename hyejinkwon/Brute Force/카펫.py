# 가로 : a 세로 : b
# a >= b
# 2a + 2b - 4 = brown
# ab = brown + yellow

def solution(brown, yellow):
    answer = []
    
    area = brown+yellow
    for a in range(1, area+1):
        if area%a == 0 :
            b = area//a
            
            if a >= b and 2*a + 2*b - 4 == brown :
                answer = [a,b]
                break

    return answer