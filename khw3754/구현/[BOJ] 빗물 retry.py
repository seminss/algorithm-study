H, W = map(int, input().split())
heights = list(map(int, input().split()))

result = 0
for i, h in enumerate(heights):
    if i == 0 or i == W-1:
        continue

    left = max(heights[:i])
    right = max(heights[i+1:])

    lower = min(left, right)

    if lower > h:
        result += lower - h

print(result)