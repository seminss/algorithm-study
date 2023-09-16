'''
def correct(s) :
    stack = []
    
    for ss in s :
        if stack == [] : 
            stack.append(ss)
        
        elif stack[-1] == "[" :
            if ss == "]" :
                stack.pop()
            else : stack.append(ss)
        
        elif stack[-1] == "{" :
            if ss == "}" :
                stack.pop()
            else : stack.append(ss)
        
        elif stack[-1] == "(" :
            if ss == ")" :
                stack.pop()
            else : stack.append(ss)
            
                
    if stack == [] :
        return True
    else :
        return False
'''

def correct(s):
    
    while True :
        if "[]" not in s and "()" not in s and "{}" not in s :
            break
        
        s = s.replace("{}","")
        s = s.replace("()","")
        s = s.replace("[]","")

    if s == "" : return True
    else : return False
            
def solution(s):
    answer = 0
    i = 0
    
    while i < len(s) :
        if correct(s) :
            answer += 1
        s = s[1:]+s[:1]
        i+=1
    
    return answer