import sys

input = sys.stdin.readline
N = int(input())
human = []

for _ in range(N) :
    x,y = map(int,input().split())
    human.append([x,y])

for i in range(N) :
    rank = 1
    for j in range(N) :
        if i!=j and human[i][0] < human[j][0] and human[i][1] < human[j][1] :
            rank += 1
    print(rank, end=" ") 