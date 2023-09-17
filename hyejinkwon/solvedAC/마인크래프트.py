import sys

input = sys.stdin.readline

N,M,B = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(N)]
floor = 0
answer = int(1e9)

for i in range(257):
    check1, check2 = 0,0

    for x in range(N):
        for y in range(M):
            if ground[x][y] < i:
                check1 += (i - ground[x][y])
            else:
                check2 += (ground[x][y] - i)
    
    inventory = check2 + B
    if inventory < check1:
        continue
    
    time = 2 * check2 + check1
    if time <= answer:
        answer = time
        floor = i
print(answer, floor)