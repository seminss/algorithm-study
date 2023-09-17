import sys
input = sys.stdin.readline

N = int(input())
stack = []
seq = 1

for i in range(N) :
    num = int(input())
    
    while seq <= num :
        stack.append(seq)
        seq += 1
        print("+")

    if stack[-1] == num :
        stack.pop()
        print("-")
    else :
        print("NO")
        break
    
    