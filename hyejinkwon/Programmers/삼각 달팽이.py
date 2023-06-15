# nxn 정사각 행렬만든 후 왼쪽으로 몰아서 생각
# 꺾어야하는 방향 고려 %3 나머지연산 이용

def solution(n):
    matrix = [[0]*n for _ in range(n)]
    answer = []
    num = 1
    x,y = -1,0 # 첫 시작 -1,0
    
    for i in range(n) :
        for j in range(i,n) :
            if i%3 == 0:
                x += 1
            if i%3 == 1 :
                y += 1
            if i%3 == 2 :
                x -= 1
                y -= 1

            matrix[x][y] = num
            num += 1

    for row in matrix :
        for col in row :
            if col :
                answer.append(col)
        
    return answer