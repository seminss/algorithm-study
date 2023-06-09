def solution(m, n, board):
    answer = 0
    row_set = set()
    
    for i in range(m) : 
        board[i] = list(board[i])
    
    while True :
        for i in range(m-1) :
            for j in range(n-1) :
                block = board[i][j]
                if block == [] :
                    continue
                if board[i+1][j] == block and board[i+1][j+1] == block and board[i][j+1] == block :
                    row_set.add((i,j))
                    row_set.add((i+1,j))
                    row_set.add((i,j+1))
                    row_set.add((i+1,j+1))
        
        # 4블록 있다면
        if row_set :
            answer += len(row_set)
            for x,y in row_set :
                board[x][y] = []
            row_set = set()
        else :
            return answer
                   
        # 윗 블록들 내려오기 (1번만)
        while True :
            moved = 0
            for i in range(m-1) :
                # 틀린이유 : column은 행과 관련없으므로 n 까지 for문 탐색 
                # n-1로 작성함
                for j in range(n) :
                    if board[i][j] and board[i+1][j] == [] :
                        board[i+1][j] = board[i][j]
                        board[i][j] = []
                        moved = 1
            if moved == 0 :
                break