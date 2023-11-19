# 10:25~45

T = int(input())


def recursive(n, m):
    if m > 1:
        return n * recursive(n, m - 1)
    else:
        return n


for i in range(10):
    index = int(input())
    n, m = map(int, input().split())
    print(f"#{index} {recursive(n, m)}")
