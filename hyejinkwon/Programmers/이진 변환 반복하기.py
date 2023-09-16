# 6 / 2 = 3 ... 0
# 3 / 2 = 1 ... 1
# 1 / 2 = 0 ... 1
def binary_num(s) :
    result = ""
    
    while s != 0 :
        result += str(s%2)  
        s //= 2
    
    return result[::-1]

def solution(s):
    answer = [0,0]
    
    while s != "1" :
        answer[1] += s.count("0")
        answer[0] += 1 
        s = str(s.count("1"))
        s = binary_num(int(s))
    
    return answer