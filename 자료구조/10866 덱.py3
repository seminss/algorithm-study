import sys

N=int(sys.stdin.readline())
deque=[]

#deque, Last in First out
for i in range(N):
    command=(sys.stdin.readline())
    if "push_front" in command:
        p_line,num=map(str,command.split())
        deque.insert(0,num)
    elif "push_back" in command:
        p_line,num=map(str,command.split())
        deque.append(num)
    elif "pop_front" in command and len(deque)!=0:
        a=deque.pop(0)
        print(a)
    elif "pop_back" in command and len(deque)!=0:
        a=deque.pop()
        print(a)
    elif "size" in command:
        print(len(deque))
    elif "empty" in command:
        if len(deque)==0:
            print(1)
        else:
            print(0)
    elif "front" in command and len(deque)!=0:
        print(deque[0])
    elif "back" in command and len(deque)!=0:
        print(deque[-1])
    else:
        print(-1)