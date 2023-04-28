import sys
from itertools import combinations

input = sys.stdin.readline

n = int(input())
n_list = list(map(int,input().split()))
sum_list = [n_list[n-1]]
sum = 0
# x1(x2 + x3 + ... + xn) + x2(x3 + x4 + ... + xn) + .. + x(n-1)x(n)
# 1(-2 + 3) + -2(3)
# 1 + -6

for i in range(n-2,0,-1) :
    sum_list.append(n_list[i] + sum_list[n-(i+2)])

sum_list = sum_list[::-1]

for i in range(n-1) :
    sum += sum_list[i]*n_list[i]
print(sum)