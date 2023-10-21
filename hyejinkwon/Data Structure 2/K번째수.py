def solution(array, commands):
    answer = []

    for i,j,k in commands :
        array_list = array
        array_list = array_list[i-1:j] 
        array_list.sort()
        answer.append(array_list[k-1])
    
    return answer