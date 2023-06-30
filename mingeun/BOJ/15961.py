# 23.7.1 00:34 ~ 

def dict_add(d:dict, k:int):
    if k in d:
        d[k] += 1
    else:
        d[k] = 1

def dict_reduce(d:dict, k:int):
    if d[k] == 1:
        del d[k]
    elif d[k] > 1:
        d[k] -= 1

n, d, k, c = map(int, input().split(' '))
dishes = [int(input()) for _ in range(n)]

ds, de = 0, 0
eat = dict()
dict_add(eat, dishes[ds])
answer = len(eat)

while ds <= n:
    # ds부터 k개 추가
    while de < ds + k - 1:
        de += 1
        dict_add(eat, dishes[de % n])
    # 쿠폰
    dict_add(eat, c)
    if len(eat) > answer:
        answer = len(eat)
    # print(f'ds: {ds} de: {de} {set(eat)}')
    # ds 한 칸 전진
    dict_reduce(eat, dishes[ds % n])
    ds += 1

print(answer)
