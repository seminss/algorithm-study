import sys
N = int(input())

schedules = []
for _ in range(N):
    schedules.append(tuple(map(int, sys.stdin.readline().split())))

schedules = sorted(schedules, key=lambda x: (x[0], -x[1]))
print(schedules)
result = 0

table = [[False for _ in range(365 + 1)]]
height = 1
width = 0
lastDay = -1
for start, end in schedules:
    for i in range(len(table)):
        if not table[i][start]:
            for j in range(start, end + 1):
                table[i][j] = True
            if lastDay + 1 >= start:
                if height < i + 1:
                    height = i + 1
                if lastDay < end:
                    width += end - lastDay
                    lastDay = end
            else:
                result += width * height
                width = end - start + 1
                height = 1
                lastDay = end
            break
    else:
        table.append([False for _ in range(365 + 1)])
        height += 1
        if lastDay < end:
            width += end - lastDay
            lastDay = end
        for j in range(start, end + 1):
            table[-1][j] = True

    print(width, result)


result += width * height
print(result)

# for l in table:
#     print(*l)