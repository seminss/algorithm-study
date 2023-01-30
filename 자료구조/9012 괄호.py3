import sys
n=int(input())
stack=[]
result=""
for i in range(n):    
    bracket=sys.stdin.readline()
    for j in range(len(bracket)-1):
        if bracket[j]=='(':
            stack.append(bracket[j])
        else: #입력: 닫는 괄호 ')'
            if len(stack)==0:
                result="NO"
                break
            stack.pop()
    if len(stack)==0 and result=="":
        result="YES"
    else:
        result="NO"
    print(result)
    result=""
    stack=[]