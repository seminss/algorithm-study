from itertools import product

N, K = map(int, input().split())
kList = list(map(int, input().split()))

numList = list(product(kList, repeat=1))
for length in range(2, len(str(N)) + 1):
    numList.extend(list(product(kList, repeat=length)))

numList = sorted(list(map(lambda l: int(''.join(map(str, l))), numList)), reverse=True)
for n in numList:
    if N >= n:
        print(n)
        break