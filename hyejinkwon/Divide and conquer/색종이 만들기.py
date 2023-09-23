# 전체 종이 모두 같은 색으로 칠해져 있지 않으면
# 가로 세로 중간부분잘라서 나눔

import sys
input = sys.stdin.readline

N = int(input())
colorpaper = []
for _ in range(N) :
    colorpaper.append(list(map(int,input().split())))
blue = 0
white = 0

def check(x,y,division) :
    global blue, white
    color = colorpaper[x][y]

    # 4사분면 확인
    for i in range(x,x+division) :
        for j in range(y,y+division) :
            if color != colorpaper[i][j] :
                check(x,y,division//2)
                check(x, y+division//2, division//2)
                check(x+division//2, y, division//2)
                check(x+division//2, y+division//2, division//2)
                return

    if color == 0 : white += 1
    else : blue += 1

check(0,0,N)
print(white)
print(blue)