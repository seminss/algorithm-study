import sys
from collections import deque
input = sys.stdin.readline
T = int(input())

# 시간 초과 발생 이유
# 뒤집는 횟수가 짝수면 origin
# 뒤집는 횟수가 홀수면 reverse

for _ in range(T) :
    comment = input().rstrip()
    l = int(input())
    li = deque(input().rstrip()[1:-1].split(","))
    
    if l == 0 :
        li = deque()
    
    rev = 0
    for c in comment :
        if c == "R" :
            rev += 1
        elif c == "D" :
            if len(li) == 0 :
                print("error")
                break
            else :
                if rev%2==0: li.popleft()
                else : li.pop()
    
    else:
        if rev%2==0 : print("["+",".join(li) + "]")
        else : 
            li.reverse()
            print("["+",".join(li) + "]")