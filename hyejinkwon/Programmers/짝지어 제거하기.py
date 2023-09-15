def solution(s):
    answer= ''
    result = []
    for i in s :
        if result == [] :
            result.append(i)
        elif result != [] and result[-1] == i :
            result.pop()
        else :
            result.append(i)
    
    if result == [] :
        answer = 1
    else :
        answer = 0
    
    return answer