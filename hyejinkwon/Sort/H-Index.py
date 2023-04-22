def solution(citations):
    answer = 0    
    # 1  index : 0  3-0 = 3
    # 4  index : 1  3-1 = 2
    # 5  index : 2  3-2 = 1
    
    citations.sort()
    
    for i,c in enumerate(citations) :
        if c >= len(citations) - i :
            answer = len(citations) - i
            break
    
    return answer