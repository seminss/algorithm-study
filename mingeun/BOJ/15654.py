'''2023.7.15
00:00 ~ 00:10
'''


def permute(answer, numbers, tmp, m):
    if len(tmp) == m:
        answer.append(list(tmp))
    else:
        for i in range(len(numbers)):
            if numbers[i] not in tmp:
                tmp.append(numbers[i])
                permute(answer, numbers, tmp, m)
                tmp.pop()


def solution():
    n, m = map(int, input().split(' '))
    numbers = list(map(int, input().split(' ')))
    answer = []
    permute(answer, sorted(numbers), [], m)
    for arr in answer:
        for num in arr:
            print(num, end = ' ')
        print()

solution()
