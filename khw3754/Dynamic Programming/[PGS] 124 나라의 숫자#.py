'''
1
2
4

11  4   1
12  5   1
14  6   2

21  7   2
22  8   2
24  9   3

41  10  3
42  11  3
44  12  4

111 13  4
112 14  4
114 15  5

121 16  5

-> 3으로 나눈 나머지가 1/2/0 에 따라 1, 2, 4 를 맨 뒤에 쌓아가면 됨
'''


def change(n):
    cha = {1: '1', 2: '2', 0: '4'}
    result = ''
    while n > 0:
        result += cha[n % 3]

        if n % 3 != 0:
            n = n // 3
        else:
            n = n // 3 - 1

    return result[::-1]


def solution(n):
    return change(n)