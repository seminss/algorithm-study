# 풀다 만 코드
# import sys
# input = sys.stdin.readline
#
# N = int(input())
# books = []
#
# for _ in range(N):
#     books.append(list(map(int, input().split())))
#
# checkedBooks = []   # [[day, Ti, Pi], ...]
# for day, book in list(enumerate(books))[::-1]:
#     Ti, Pi = book
#     if day + Ti > len(books):
#         continue
#
#     # checked 에 있는 예약 중에 이익을 따져봐야함
#     for checked in checkedBooks[::-1]:
#         if

import sys
input = sys.stdin.readline

N = int(input())
books = [0] * (N + 1)

for day in range(N):
    Ti, Pi = map(int, input().split())
    if Ti != 1 and books[day] > books[day + 1]:
        books[day + 1] = books[day]
    if day + Ti > N:
        continue

    if books[day] + Pi > books[day + Ti]:
        books[day + Ti] = books[day] + Pi

print(books[-1])