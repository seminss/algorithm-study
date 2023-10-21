def solution(n, times):
    answer = 0
    start, end = 1, max(times)*n
    
    while start <= end :
        mid = (start+end)//2
        person = 0 
        for t in times :
            person += mid//t 
        
            if person >= n : break
            
        if person >= n :
            answer = mid
            end = mid-1
        else : 
            start = mid+1
            
    return answer