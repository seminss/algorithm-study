H, W = map(int, input().split())
heights = list(map(int, input().split()))

result = 0
left, right = -1, -1

hDict = {i : [] for i in range(H+1)}
for i, h in enumerate(heights):
    hDict[h].append(i)


# 다 돌면서 각 높이의 좌표를 저장해둠
# 가장 높은 높이부터 다 처리

for h in range(H, -1, -1):
    if len(hDict[h]) == 1:
        if left == -1:
            left, right = hDict[h][0], hDict[h][0]
        else:
            if left > hDict[h][0]:
                for i in range(hDict[h][0]+1, left):
                    result += h - heights[i]
                left = hDict[h][0]
            if right < hDict[h][0]:
                for i in range(right+1, hDict[h][0]):
                    result += h - heights[i]
                right = hDict[h][0]

    elif len(hDict[h]) > 1:
        nLeft, nRight = hDict[h][0], hDict[h][-1]
        if left == -1:
            for i in range(nLeft + 1, nRight):
                result += h - heights[i]
            left, right = nLeft, nRight
        else:
            if left > nLeft:
                for i in range(nLeft+1, left):
                    result += h - heights[i]
                left = nLeft
            if right < nRight:
                for i in range(right+1, nRight):
                    result += h - heights[i]
                right = nRight
print(result)