# 2:52~3:17
import sys


def pooling(sq):
    new_len = len(sq)//2
    new_sq = [[0] * new_len for _ in range(new_len)]
    if len(sq) == 1:
        print(sq[0][0])
        return
    for i in range(new_len):
        for j in range(new_len):
            new_sq[i][j] = sorted([sq[i*2][j*2], sq[i*2][j*2 + 1], sq[i*2 + 1][j*2], sq[i*2 + 1][j*2 + 1]])[2]
    pooling(new_sq)


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    maps = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    pooling(maps)