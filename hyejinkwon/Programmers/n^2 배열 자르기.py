def solution(n, left, right):
    answer = []
    map = []
    
    # 행 열 위치 : index//n, index%n
    # max(index//n, index%n) + 1
    
    for i in range(left,right+1):
        map.append(max([i//n, i%n])+1)
        
    answer = map
        
    return answer