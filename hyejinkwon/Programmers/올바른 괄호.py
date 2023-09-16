def solution(s):
    answer = True
    stack = []
    
    for index,i in enumerate(s) :
        if i == "(" : 
            stack.append("(")
        elif len(stack) != 0 and i == ")" :
            stack.pop()
        elif i == ")" and index == 0 :
            answer = False
            return answer
    
    if stack == [] :
        answer = True
    else :
        answer = False

    return answer