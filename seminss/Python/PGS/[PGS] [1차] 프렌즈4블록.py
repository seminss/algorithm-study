# 터뜨려야 하는 위치를 set으로 저장, 한바퀴 다 돌면 한번에 해당 좌표 비우기
dx=[1,0,1]
dy=[0,1,1]

def isSquare(x,y,maps):
    s=maps[y][x]
    for i in range(3):
        nx=x+dx[i]
        ny=y+dy[i]
        if maps[ny][nx]!=s:
            return False
    return True
    
def solution(m, n, board):
    answer=0
    rotation=[['']*m for _ in range(n)] 
    
    for i in range(n):
        for j in range(m):
            rotation[i][j]=board[j][i]
            
    while True:
        pang=set() #rotation의 높이:n, 폭:m
        for i in range(n-1):
            for j in range(m-1):
                if rotation[i][j]!='*' and isSquare(j,i,rotation):
                    pang.update([(j,i),(j+1,i),(j,i+1),(j+1,i+1)])
        if len(pang)==0:
            break
        else:
            answer+=len(pang)
            while pang:
                p=pang.pop()
                x,y=p[0],p[1]
                rotation[y][x] = '*'
            for r in rotation:
                count_star = r.count('*')
                others = [x for x in r if x != '*']
                r[:count_star] = ['*'] * count_star
                r[count_star:] = others 
                #그냥 r = ['*'] * count_star + others 하면 원소 교체가 완전 일어나지 않음. 슬라이싱 해서 바꿔야함
                
    return answer