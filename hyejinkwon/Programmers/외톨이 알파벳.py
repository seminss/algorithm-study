def solution(input_string):
    answer = ''
    choice = input_string[0]
    count_dict = {}
    N = len(input_string)
    answer_list = []
    
    
    for i in range(N-1) :
        if input_string[i] != input_string[i+1] : 
            choice += input_string[i+1]
        #else : # 연속 같은 글자
        
    for c in choice :
        if c in count_dict : count_dict[c] += 1
        else : count_dict[c] = 1
        
    for key, value in count_dict.items() :
        if value >= 2 :
            answer_list.append(key)
    
    if answer_list == [] :
        answer = "N"
    else :
        answer_list.sort()
        for a in answer_list :
            answer += a
    
    return answer