import sys

input = sys.stdin.readline

N = int(input())

def VPS(s) :
    stack = []
    for ss in s :
        if stack == [] :
            stack.append(ss)
        elif stack[-1] == "(":
            if ss == ")" : stack.pop()
            else : stack.append(ss)

    if stack == [] :
        return True
    else :
        return False

for _ in range(N) : 
    if VPS(input().rstrip()) :
        print("YES")
    else:
        print("NO")