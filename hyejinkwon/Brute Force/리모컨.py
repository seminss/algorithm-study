import sys

input = sys.stdin.readline
N = int(input())
M = int(input())
if M != 0 :
    no_button = list(input().split())
else :
    no_button = []

answer = abs(100-N)

for i in range(1000001) :
    for ii in str(i) :
        if ii in no_button:
            break   
    else :
        answer = min(answer, len(str(i))+abs(i-N) )

print(answer)