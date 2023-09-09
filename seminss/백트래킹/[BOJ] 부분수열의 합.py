import sys

N, S = map(int, sys.stdin.readline().split())
data = sorted(list(map(int, sys.stdin.readline().strip().split())))
res = []
answer = 0


def back(start):
    global res, answer
    if sum(res) == S and len(res) != 0:
        answer += 1
    if start == len(data):
        return
    for i in range(start, len(data)):
        res.append(data[i])
        back(i + 1)
        res.pop()


back(0)
print(answer)
