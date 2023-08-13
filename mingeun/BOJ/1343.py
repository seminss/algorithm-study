'''2023.8.10
15:54 ~ 16:38
'''


def fill_board(s, e):
    number_of_x = e - s
    result = ''
    while number_of_x > 0:
        if number_of_x//4 > 0:
            result += 'AAAA' * (number_of_x//4)
            number_of_x %= 4
        elif number_of_x//2 > 0:
            result += 'BB' * (number_of_x//2)
            number_of_x %= 2
        else:
            raise Exception
    return result


def solution():
    board = input()
    answer = ''
    idx, end_of_x_idx = 0, 0
    while idx < len(board):
        # . 건너뜀
        while idx < len(board) and board[idx] == '.':
            idx += 1
            answer += '.'
        end_of_x_idx = idx
        # 연속된 X를 폴리노미노로 바꾼다.
        while end_of_x_idx < len(board) and board[end_of_x_idx] == 'X':
            end_of_x_idx += 1
        try:
            answer += fill_board(idx, end_of_x_idx)
        except Exception:
            print(-1)
            return
        idx = end_of_x_idx
    print(answer)


solution()
