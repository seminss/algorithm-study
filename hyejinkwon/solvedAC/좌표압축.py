import sys
input = sys.stdin.readline

N = int(input())
point = list(map(int, input().split()))
repoint = sorted(list(set(point)))

answer ={}

for i in range(len(repoint)) :
    answer[repoint[i]] = i

for i in point :
    print(answer[i], end=" ")