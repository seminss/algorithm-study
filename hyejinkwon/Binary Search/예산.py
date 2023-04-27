import sys

input = sys.stdin.readline

N = int(input())
money_list = list(map(int,input().split()))
total = int(input())

start, end = 0, max(money_list)

# 모든 요청 배정 가능 -> 요청한 금액 그대로 배정
if sum(money_list) <= end :
    print(max(money_list))

# 모든 요청 배정 불가능 -> 특정한 정수 상한액 계산하여 그 이상인 예산요청에는 모두 상한액을 배정
# 상한액 이하의 예산요청에 대해서는 요청한 금액을 그대로 배정
else : 
    while start <= end :
        mid = (start+end) // 2

        sum_money = 0
        for m in money_list :
            if m <= mid :
                sum_money += m
            else :
                sum_money += mid

        if sum_money > total :
            end = mid - 1
        else :
            start = mid + 1

    print(end)