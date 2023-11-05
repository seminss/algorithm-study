def solution(s):
    stack=[]
    for i in s:
        if i=="(":
            stack.append(i)
        elif len(stack)==0 or stack.pop()!='(':
                return False
    if len(stack)==0:
        return True
    else:
        return False