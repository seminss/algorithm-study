import sys

n,m=map(int,sys.stdin.readline().split())
maps=[[0]*(m) for _ in range(n)]
def dfs(x,y:list)->int:
    count=0
    if y>=m:
        x=x+1
        y=0
    if x>=n:
        return 0
    
    if maps[x][y-1] ==0 or maps[x-1][y-1]==0 or maps[x-1][y]==0:
        maps[x][y]=1
        count+=dfs(x,y+1)+1
        maps[x][y]=0

    count+=dfs(x,y+1)
    return count
print(dfs(0,0)+1)
