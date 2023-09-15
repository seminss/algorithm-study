def solution(n):
    answer = 0
    
    for i in range(1, n//2+1) :
        result = i
        for j in range(i+1,n//2+2) :
            result += j
            if result == n :
                answer += 1
                break
                
            if result > n : 
                break    
        
    answer += 1 # 자기자신 
    return answer