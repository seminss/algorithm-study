import sys
input = sys.stdin.readline
N = int(input())
coordinate = []

for _ in range(N) :
    x,y = map(int, input().split())
    coordinate.append([x,y])

coordinate = sorted(coordinate, key=lambda x : (x[0], x[1]))
for x,y in coordinate :
    print(x,y)