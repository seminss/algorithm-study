x, y = map(int, input().split())
xy = x*y
if x < y:
    x, y = y, x

while y != 0:
    x, y = y, x%y

print(x)
print(xy//x)