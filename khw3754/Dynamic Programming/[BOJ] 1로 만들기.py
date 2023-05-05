n = int(input())

# 1, 2, 3 넣음
l = [0, 0, 1, 1]

for i in range(4, n+1):
    tmp = [l[i-1] + 1]
    if i % 2 == 0:
        tmp.append(l[i//2] + 1)
    if i % 3 == 0:
        tmp.append(l[i//3] + 1)
    l.append(min(tmp))

print(l[n])