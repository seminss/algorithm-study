import sys

input = sys.stdin.readline
N,M,B = map(int,input().split())
ground = []
floor = 0
time = int(1e9)

ground = [list(map(int, input.split())) for _ in range(N)]

for i in range(257) :
    check_1 = 0
    check_2 = 0
    for x in range(N) :
        for y in range(M) :
            if ground[x][y] > i :
                check_2 += ground[x][y] - i
            else :
                check_1 += i - ground[x][y]

    if check_1 <= check_2 + B :
        
        if check_2*2 + check_1 <= int(1e9) :
            time = check_2*2 + check_1
            floor = i
print(time, floor)
