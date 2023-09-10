'''2023.7.24
-1
'''


def solution():
    n, m = map(int, input().split(' '))
    mars = [list(map(int ,input().split(' '))) for _ in range(n)]
    # DP
    # 첫 번째 행 업데이트 (오른쪽으로만 진행 가능)
    for y in range(1, m):
        mars[0][y] += mars[0][y-1]
    # 나머지 값 업데이트
    for x in range(1, n):
        left2right = mars[x][:]
        right2left = mars[x][:]
        # 왼쪽에서 오른쪽으로만 이동하는 경우
        for y in range(m):
            if y == 0:
                left2right[y] += mars[x-1][y]
            else:
                left2right[y] += max(mars[x-1][y], left2right[y-1])
        # 오른쪽에서 왼쪽으로만 이동하는 경우
        for y in range(m - 1, -1, -1):
            if y == m - 1:
                right2left[y] += mars[x-1][y]
            else:
                right2left[y] += max(mars[x-1][y], right2left[y+1])
        # 값 결정
        for y in range(m):
            mars[x][y] = max(left2right[y], right2left[y])
    print(mars[n-1][m-1])


solution()
