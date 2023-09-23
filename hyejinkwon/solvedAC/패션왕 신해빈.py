import sys

input = sys.stdin.readline
T = int(input())


for _ in range(T) :
    N = int(input())
    clothes_kind = dict()
    answer = 1

    for _ in range(N) :
        name, kind = input().split()

        if kind in clothes_kind : clothes_kind[kind] += 1
        else : clothes_kind[kind] = 1

    for kind, count in clothes_kind.items() :
        answer *= count + 1

    print(answer-1)