import sys

input = sys.stdin.readline
N = input()

def Factorial(N) :
    answer = 1
    while N != 0:
        answer *= N
        N -= 1
        
    return answer

N = str(Factorial(int(N)))
N = N[::-1]
zero = False
answer = 0 

for n in N :
    if n != "0" :
        break
    answer += 1
    
print(answer)    