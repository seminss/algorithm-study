import sys

input = sys.stdin.readline

N = int(input())
answer = 1
i = 1

while i < N :
    i += 6*answer
    answer += 1

print(answer)