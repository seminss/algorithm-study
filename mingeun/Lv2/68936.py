'''2023.6.9
16:17 ~ 17:00 
20:50 ~ 21:02
'''
ZERO = 0
ONE = 0
def check_square(arr, xs, xe, ys, ye):
    """
    구역 내의 모든 원소 값이 같은지 확인한다.
    """
    n = arr[xs][ys]
    for i in range(xs, xe+1):
        for j in range(ys, ye+1):
            if arr[i][j] != n:
                return False
    return True


def dfs(arr, xs, xe, ys, ye):
    """
    xs, xe: x방향 시작, 끝(include) 인덱스
    ys, ye: y방향 시작, 끝(include) 인덱스
    구역 내의 모든 원소의 값이 같을때까지 네 부분으로 나눈다.
    """
    global ONE
    global ZERO
    if check_square(arr, xs, xe, ys, ye):
        # print(f'x: {xs}, {xe} y: {ys}, {ye} value: {arr[xs][ys]}')
        if arr[xs][ys] == 0:
            ZERO += 1
        elif arr[xs][ys] == 1:
            ONE += 1
        return
    else:
        '''
        x: xs - xs/2 | xs/2+1 - xe
        y: ys - ys/2 | ys/2+1 - ye
        '''
        xm, ym = (xs + xe) // 2, (ys + ye) // 2
        dfs(arr, xs, xm, ym+1, ye) # 1사분면
        dfs(arr, xs, xm, ys, ym) # 2사분면
        dfs(arr, xm+1, xe, ys, ym) # 3사분면
        dfs(arr, xm+1, xe, ym+1, ye) # 4사분면
        return


def solution(arr):
    n = len(arr)
    dfs(arr, 0, n-1, 0, n-1)
    return [ZERO, ONE]
