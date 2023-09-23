import sys

input = sys.stdin.readline

L = int(input())
s = input().rstrip()
answer = 0

for i in range(L) :
    answer += (ord(s[i])-96) * (31**i)
print(answer % 1234567891)
