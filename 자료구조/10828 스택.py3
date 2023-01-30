import sys

N=int(sys.stdin.readline())
stack=[]

for i in range(N):
    command=(sys.stdin.readline())
    if "push" in command:
        p_line,num=map(str,command.split())
        stack.append(int(num))
    elif "pop" in command:
        if len(stack)==0:
            print(-1)
        else:
            a=stack.pop()
            print(a)
    elif "size" in command:
        print(len(stack))
    elif "empty" in command:
        if len(stack)==0:
            print(1)
        else:
            print(0)
    elif "top" in command:
        if len(stack)==0:
            print(-1)
        else:
            a=stack.pop()
            print(a)
            stack.append(a)