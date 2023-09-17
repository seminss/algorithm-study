import sys
input = sys.stdin.readline

N = int(input())
stack = []
answer = []
No = False
seq = 1

for i in range(N) :
    num = int(input())
    
    while seq <= num :
        stack.append(seq)
        seq += 1
        answer.append("+")

    if stack[-1] == num :
        stack.pop()
        answer.append("-")
    else :
        No = True
        break
if No :
    print("NO")
else : 
    for a in answer :
        print(a)
    
    