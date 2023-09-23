import sys

input = sys.stdin.readline
N = int(input())
INF = 10001
list = [0] * INF

# append 메모리 초과
for _ in range(N) :
    list[int(input())] += 1

for i in range(INF):
    if list[i] != 0 :
        for _ in range(list[i]) :
            print(i)