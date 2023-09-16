def solution(n):
    answer = 0
    
    one_count = bin(n).count("1")
    while 1 :
        n = n +1
        if one_count == bin(n).count("1") :
            answer = n
            break
    
    return answer