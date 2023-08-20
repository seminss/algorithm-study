'''2023.8.12
23:10 ~ 23:18
'''
import sys


def calculate_tip(before, order_num):
    tip = before - (order_num-1)
    return tip if tip > 0 else 0


def solution():
    # n <= 10^5
    n = int(sys.stdin.readline())
    tips = [int(sys.stdin.readline()) for _ in range(n)]
    tips.sort(reverse=True)
    answer = 0
    for i, tip in enumerate(tips):
        order = i + 1
        answer += calculate_tip(tip, order)
    print(answer)


solution()
