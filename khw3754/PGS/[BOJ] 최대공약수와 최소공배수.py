from collections import defaultdict
x, y = map(int, input().split())
x_dict = defaultdict(int)
y_dict = defaultdict(int)

def make_dict(n, d):
    while n != 1:
        for i in range(2, n+1):
            if n % i == 0:
                d[i] += 1
                n = n//i
                break
# 소인수분해
make_dict(x, x_dict)
make_dict(y, y_dict)

m = 1
# 최대공약수 계산
for k in x_dict.keys():
    if y_dict.get(k, -1) != -1:
        m *= k**min(x_dict[k], y_dict[k])
print(m)

# 최소공배수 계산
s = list(x_dict.keys())
s.extend(y_dict.keys())
s = list(set(s))
m = 1
for k in s:
    m *= k ** max(x_dict.get(k, -1), y_dict.get(k, -1))
print(m)