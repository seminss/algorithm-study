# 가로 : a 세로 : b
# a >= b
# 2a + 2b - 4 = brown
# (a-2)*(b-2) = yellow
# ab = brown + yellow
# ab = 3a + 3b -8

def divisor(number) :
    divisor_list = []
    for i in range(1, number**(1//2)+1) :
        if number % i == 0:
            divisor_list.append(i)
            if i < number // i :
                divisor_list.append(i)
                
        divisor_list.sort()
    return divisor_list
    

def solution(brown, yellow):
    answer = []
    carpet = brown+yellow
    
    divisor_list = divisor(carpet)
    
    for b in range(1,carpet + 1):
        # 나누어 떨어져야 함
        if carpet%b == 0 :
            a = carpet // b
            if a >= b and brown == 2*a+2*b-4 :
                break
    answer = [a,b]
    return answer