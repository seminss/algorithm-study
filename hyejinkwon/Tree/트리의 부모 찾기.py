import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N+1)]
parent = [0] * (N+1)

for i in range(N-1) :
    a,b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

print(tree)

def DFS(start, tree, parent) :
    for i in tree[start] :
        if parent[i] == 0 :
            parent[i] = start
            DFS(i, tree, parent)

DFS(1, tree, parent)

for i in range(2, N+1) :
    print(parent[i])