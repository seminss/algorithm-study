import sys

input = sys.stdin.readline

n,m = map(int,input().split())
parent = [i for i in range(n+1)]

# 루트 노드 찾기
def find(a) :
    if a == parent[a] :
        return a
    p = find(parent[a]) # 루트노드 찾기
    parent[a] = p # 부모 테이블 갱신
    return parent[a]

def union(a,b) : 
    a = find(a)
    b = find(b)

    if a==b :
        return 
    if a<b :
        parent[b] = a
    else :
        parent[a] = b

for _ in range(m) :
    c,a,b = map(int, input().split())

    if c == 0 :
        union(a,b)
    print(parent)
    if c == 1 :
        if find(a) == find(b) :
            print("YES")
        else :
            print("NO")