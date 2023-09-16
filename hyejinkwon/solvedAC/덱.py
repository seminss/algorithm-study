import sys
from collections import deque

input = sys.stdin.readline

N = int(input().rstrip())
deque = deque([])
for _ in range(N) :
    command = input()
    if "push_back" in command : 
        com, num = command.split()
        deque.append(int(num))
    elif "push_front" in command :
        com, num = command.split()
        deque.appendleft(int(num))
    elif "front" == command :
        if len(deque) == 0 : print(-1)
        else : print(deque[0])
    elif "back" == command : 
        if len(deque) == 0 : print(-1)
        else : print(deque[-1])
    elif "empty" == command : 
        if len(deque) == 0 : print(1)
        else : print(0)
    elif "size" == command :
        print(len(deque))
    elif "pop_front" == command : 
        if len(deque) == 0 :print(-1)
        else: print(deque.popleft())
    elif "pop_back" == command :
        if len(deque) == 0 :print(-1)
        else: print(deque.pop())
    print(deque)