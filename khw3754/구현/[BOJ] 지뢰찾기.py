n = int(input())
mapp = []
result = []

for _ in range(n):
    mapp.append(input())

dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]


def count(x, y):
    count = 0
    for i in range(8):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if mapp[nx][ny] == '*':
                count += 1
    return count

over = False

for i in range(n):
    line = input()
    addLine = ''
    for j in range(n):
        if line[j] == 'x':
            if mapp[i][j] == '*':
                over = True
            addLine += str(count(i, j))
        else:
            addLine += '.'
    result.append(addLine)

if over:
    for i in range(n):
        for j in range(n):
            if mapp[i][j] == '*':
                result[i] = result[i][:j] + '*' + result[i][j+1:]

for r in result:
    print(r)