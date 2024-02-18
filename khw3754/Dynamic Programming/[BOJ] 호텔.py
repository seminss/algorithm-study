C, N = map(int, input().split())
ads = []
for _ in range(N):
    ads.append(list(map(int, input().split())))

result = [-1] * (C + 1)
result[0] = 0

goals = []
for i in range(C):
    if result[i] != -1:
        for pay, count in ads:
            if i + count < C and (result[i + count] == -1 or result[i + count] > result[i] + pay):
                result[i + count] = result[i] + pay
            elif i + count >= C:
                goals.append(result[i] + pay)

print(min(goals))