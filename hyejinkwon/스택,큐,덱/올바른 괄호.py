def correct(string) : 
    # ())(()
    stack = []
    for i, s in enumerate(string) :
        if i == 0 and s != '(': # 시작부터 "(" 아니라면 return False
            return False           
        
        if s == "(" : 
            stack.append('(')
            
        elif s == ")" and len(stack) != 0 :
            stack.pop()
        else :
            return False
        
    return len(stack) == 0
    # if stack != [] :
    #     return False
    # else:
    #     return True
            

def solution(s):
    answer = True
    answer = correct(s)

    return answer