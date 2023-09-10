'''
1 = 1
2 = 2
3 = 3
111
12

4의 경우  1+3+1 = 5
1111
112
22

5는      1+3+4 = 8
11111
1112
122

6은      1+5++1 =
111111
11112
1122
222
'''


def solution(n):
    if n == 1:
        return 1

    a, b = 1, 2
    for _ in range(n - 2):
        a = a + b
        a, b = b, a

    return b % 1_000_000_007

#     l = [1, 2]
#     for i in range(n-2):
#         l.append(l[-1] + l[-2])

#     if n == 1:
#         return 1
#     else:
#         return l[-1] % 1_000_000_007

# from itertools import permutations as permut

# def solution(n):
#     answer = 0

#     s1 = '1' * n
#     s2 = ''
#     while len(s1) > 1:
#         answer += len(set(permut(s1 + s2)))
#         s1 = s1[2:]
#         s2 += '2'

#     answer += len(set(permut(s1 + s2)))

#     return answer

