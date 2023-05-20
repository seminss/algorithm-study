''' 2023.5.20
15:15 ~ 
'''
def solution(dirs):
    answer = 0
    pos = [0, 0]
    X, Y = 0, 1
    visited = set()
    # U R D L
    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
    for d in dirs:
        i = 'URDL'.index(d)
        x, y = pos[X], pos[Y]
        xn, yn = pos[X] + dx[i], pos[Y] + dy[i]
        move = str(pos[X]) + str(pos[Y]) + str(xn) + str(yn)
        move_reversed = str(xn) + str(yn) + str(pos[X]) + str(pos[Y])
        if -5<=xn<=5 and -5<=yn<=5:
            pos[X], pos[Y] = xn, yn
            if move not in visited:
                answer += 1
                visited.add(move)
                visited.add(move_reversed)
                # print(f'({x}, {y}) -> {pos} {visited}')
    return answer
