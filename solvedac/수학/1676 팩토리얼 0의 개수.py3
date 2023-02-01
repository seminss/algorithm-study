import sys

n = int(sys.stdin.readline())
mul = 1
for i in range(1,n+1):
    mul *= i

lst = list(str(mul))
idx = len(lst)-1
cnt = 0

while lst[idx] == '0':
    cnt += 1
    idx -= 1
print(cnt)