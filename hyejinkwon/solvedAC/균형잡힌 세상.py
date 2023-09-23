import sys

input = sys.stdin.readline
s = ""

while s !="." :
    s = input().rstrip()
    if s == "." :
        break
    stack = []

    for ss in s :
        if ss == "(" or ss =="[" :
            stack.append(ss)
        
        elif ss == ")":
            if stack!=[] and stack[-1] == "(" : 
                stack.pop()
            else :
                stack.append(")") 
                break
        elif ss == "]":
            if stack!=[] and stack[-1] == "[" :
                stack.pop()
            else :
                stack.append("]")
                break 
    
    if stack == [] : print("yes")
    else : print("no")