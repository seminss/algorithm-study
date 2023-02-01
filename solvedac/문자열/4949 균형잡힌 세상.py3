import sys
stack=[]
result=""

sentence=sys.stdin.readline()
while True:
    if sentence=='.\n':
        exit()

    for i in range(len(sentence)-1):
        if sentence[i]=='(':
            stack.append(sentence[i])
        elif sentence[i]==')':
            if len(stack)==0 or stack[-1]=="[":
                result="oh NO"
                break
            stack.pop()
        elif sentence[i]=='[':
            stack.append(sentence[i])
        elif sentence[i]==']':
            if len(stack)==0 or stack[-1]=="(":
                result="ohhhhhhh NO"
                break
            stack.pop()

    if len(stack)==0 and result=="":
        result="yes"
    else:
        result="no"
    print(result)

    result="" 
    stack=[]
    sentence=sys.stdin.readline()
