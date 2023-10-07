import sys

N = int(sys.stdin.readline())
nodes = {}
for _ in range(N):
    a, b, c = map(int, sys.stdin.readline().split())

    if nodes.get(a, -1) == -1:
        nodes[a] = [b, c, -1]
    else:
        nodes[a][0], nodes[a][1] = b, c

    # 자식들
    if nodes.get(b, -1) == -1:
        nodes[b] = [-1, -1, a]
    else:
        nodes[b][2] = a
    if nodes.get(c, -1) == -1:
        nodes[c] = [-1, -1, a]
    else:
        nodes[c][2] = a

# 먼저 중위 순회의 마지막 노드를 구함
lastNodeNum = 0
pos = 1
while True:
    if nodes[pos][1] != -1:
        pos = nodes[pos][1]
    else:
        lastNodeNum = pos
        break

# 유사 중위 순회
moveCount = 0
pos = 1
visited = [False for _ in range(N + 1)]
while True:
    leftChild = nodes[pos][0]
    rightChild = nodes[pos][1]
    if leftChild != -1 and not visited[leftChild]:
        pos = leftChild
        visited[leftChild] = True
        moveCount += 1
    elif rightChild != -1 and not visited[rightChild]:
        pos = rightChild
        visited[rightChild] = True
        moveCount += 1
    elif lastNodeNum == pos:
        break
    else:
        pos = nodes[pos][2]
        moveCount += 1

print(moveCount)