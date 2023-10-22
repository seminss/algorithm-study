N = int(input())
meetings = [list(map(int, input().split())) for _ in range(N)]

meetings = sorted(meetings, key=lambda x: (x[1], x[0]))

time = 0
count = 0
for start, end in meetings:
    if start >= time:
        count += 1
        time = end

print(count)