import sys

N, M = map(int, sys.stdin.readline().split())
data = sorted(list(map(int, sys.stdin.readline().strip().split())))
ans = []
answer=[]


def back(start):
    if len(ans) == M:
        tmp=" ".join(map(str,ans))
        if tmp not in answer:
            answer.append(tmp)
        return
    for i in range(start, len(data)):
        ans.append(data[i])
        back(i+1)
        ans.pop()

back(0)

for ans in answer:
    print(ans)