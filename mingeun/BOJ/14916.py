'''2023.8.10
-1
'''


def solution():
    # 2원, 5원 -> n원
    n = int(input())
    answer = 0
    while n > 0:
        if n % 5 == 0:
            answer += n//5
            n %= 5
        else:
            answer += 1
            n -= 2
    if n == 0:
        print(answer)
    elif n < 0:
        print(-1)

solution()
