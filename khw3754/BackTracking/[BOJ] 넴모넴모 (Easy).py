N, M = map(int, input().split())

mapp = [[0 for i in range(M)] for j in range(N)]

# x, y에 놓으면 넴모가 없어지는 지 체크하는 함수
def check(x, y):
    if x > 0:
       if y > 0 and mapp[x-1][y-1] == 1 and mapp[x][y-1] == 1 and mapp[x-1][y] == 1:
           return False
       if y < M-1 and mapp[x-1][y+1] == 1 and mapp[x-1][y] == 1 and mapp[x][y+1] == 1:
           return False
    if x < N-1:
        if y > 0 and mapp[x+1][y-1] == 1 and mapp[x+1][y] == 1 and mapp[x][y-1] == 1:
           return False
        if y < M-1 and mapp[x+1][y+1] == 1 and mapp[x+1][y] == 1 and mapp[x][y+1] == 1:
           return False

    return True

def next_pos(x, y):
    if y == M-1:
        return x+1, 0
    else:
        return x, y+1

def pm():
    for i in mapp:
        print(*i)
    print()

def dfs(x, y):
    if x == N-1 and y == M-1:
        # pm()
        if check(x, y):
            return 2
        else:
            return 1

    count = 0
    nx, ny = next_pos(x, y)
    # 놓을 수 있는 상황이면 놓는 경우, 안 놓는 경우 둘 다 생각
    if check(x, y):
        mapp[x][y] = 1
        count += dfs(nx, ny)

        mapp[x][y] = 0
        count += dfs(nx, ny)

        return count

    # 놓을 수 없는 상황이면, 안 놓는 경우만 생각
    else:
        mapp[x][y] = 0
        count += dfs(nx, ny)

        return count

print(dfs(0, 0))