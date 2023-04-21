def correct(s) :
    stack =[]
    for s_i in s :
        if s_i == "(" :
            stack.append("(")
        elif s_i == "{" :
            stack.append("{")
        elif s_i == "[" :
            stack.append("[")
            
        elif s_i == ")" :
            if stack != []:
                t = stack.pop()
                if t != "(" :
                    return False
            else :
                return False
            
        elif s_i == "}" :
            if stack != []:
                t = stack.pop()
                if t != "{" :
                    return False
            else :
                return False
        elif s_i == "]" :
            if stack != []:
                t = stack.pop()
                if t != "[" :
                    return False
            else :
                return False
            
    if stack == []  : 
        return True
    else :
        return False
            
def solution(s):
    answer = 0
    i = 0 
    
    while i < len(s) :
        first_word = s[0]
        s = s[1:] + first_word
        i += 1
        if correct(s) : 
            answer += 1
    
    return answer