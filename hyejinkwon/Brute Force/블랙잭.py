# 3장 골라 그 합이 M을 넘지 않으며 가장 가까운 수를 만들자
import sys
from itertools import combinations

N,M = map(int, input().split())
number = list(map(int,input().split()))
sum_list = list(combinations(number, 3))
max_sum = 0

for s in sum_list :
    if sum(s) <= M :
        max_sum = max(max_sum,sum(s))

print(max_sum)