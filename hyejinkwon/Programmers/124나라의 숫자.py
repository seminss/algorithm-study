def solution(n):
    answer = ''
    
    while n > 0 :
        if n%3 == 0 :
            answer += "4"
            n = n//3 - 1
        if n%3 == 1 :
            answer += str(n%3)
            n //= 3
        if n%3 == 2  :
            answer += str(n%3)
            n //= 3
    
    # answer 뒤집어서 정답처리 
    return answer[::-1]