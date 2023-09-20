import sys

input =sys.stdin.readline
N = int(input())
M = int(input())
S = input().rstrip()
L, R, count = 0,0,0

while R < M :
    if S[R:R+3] == "IOI" :
        R += 2
    
        if R-L == 2*N :
            count += 1
            L += 2

    else :
        R += 1
        L = R

print(count)