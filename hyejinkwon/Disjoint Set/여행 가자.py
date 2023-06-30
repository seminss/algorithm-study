import sys
input = sys.stdin.readline

N = int(input())
M = int(input()) # 여행계획 도시 수
city = []
parent = [i for i in range(N)]

def find(a) :
    if a != parent[a] :
        parent[a] = find(parent[a])
    return parent[a]

def union(a,b) :
    a,b = find(a), find(b)
    
    if a == b :
        return
    elif a> b :
        parent[a] = b
    else : # a<=b
        parent[b] = a

for i in range(N) :
    city.append(list(map(int, input().split())))
    for j in range(N) :
        if city[i][j] == 1 :
            union(i,j)
            
parent = [-1] + parent
plan = list(map(int, input().split()))
root = parent[plan[0]]
for i in range(1, M) :
    if root != parent[plan[i]] :
        print("NO")
        break
else :
    print("YES")
