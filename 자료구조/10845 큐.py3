import sys

N=int(sys.stdin.readline())
queue=[]
front=rear=0 #front: dequeue 위치, rear: enqueue 위치
#queue, Last in First out
for i in range(N):
    command=(sys.stdin.readline())
    if "push" in command:
        p_line,num=map(str,command.split())
        queue.append(int(num))
    elif "pop" in command:
        if len(queue)==0:
            print(-1)
        else:
            a=queue.pop(0)
            print(a)
    elif "size" in command: #o
        print(len(queue))
    elif "empty" in command: #o
        if len(queue)==0:
            print(1)
        else:
            print(0)
    elif "front" in command:
        if len(queue)==0:
            print(-1)
        else:
            print(queue[0])
    elif "back" in command:
        if len(queue)==0:
            print(-1)
        else:
            print(queue[-1])