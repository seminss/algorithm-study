def solution(s):
    answer = []
    set_list = []
    ss = ''
    
    for i in range(len(s)-1) :
        if s[i] == "{" :
            test = []
        if s[i].isdigit() :
            ss += s[i]
            if s[i+1].isdigit() :
                continue
            else :
                test.append(int(ss))
                ss = ''
        if s[i] == "}" :
            set_list.append(test)
                
    set_list = sorted(set_list, key=lambda x : len(x))
            
    for i in set_list:
        for j in i :
            if j not in answer :
                 answer.append(j)
    
    return answer