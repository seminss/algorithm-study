import sys
input = sys.stdin.readline

N = int(input())
point = list(map(int, input().split()))
repoint = sorted(list(set(point)))

# -10 -9 2 2 4
# -10 -9 2 4 (set)


answer ={}

for i in range(len(repoint)) :
    answer[repoint[i]] = i

for i in point :
    print(answer[i], end=" ")