def solution(skill, skill_trees):
    answer = 0
    linked_list = []
    
    for s in skill_trees :
        check_list = []
        
        for s_i in s :
            if s_i in skill :
                check_list.append(s_i)
        
        for i, word in enumerate(check_list) :
            if skill[i%len(skill)] != word : 
                print("not")
                break
        else : 
            answer += 1
    
    return answer