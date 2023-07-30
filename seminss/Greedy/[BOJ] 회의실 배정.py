import sys

n = int(sys.stdin.readline())
times = []
for _ in range(n):
    start, end = map(int, sys.stdin.readline().split())
    times.append((start, end))

# 종료 시간이 빠른 걸로 정렬, 같은 거는 시작 시간이 빠른 걸로 정렬 ( (5,10) (10,10) 이 있을 때 (5,10)을 먼저 해야 둘다 가능)

times.sort(key=lambda x: (x[1], x[0]))
ing = times[0]
answer = 1

for time in times[1:]:
    if time[0] >= ing[1]:
        ing = time
        answer += 1

print(answer)
