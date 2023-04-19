# N <= M
# N 만큼의 다리 짓기

import sys
from itertools import combinations

input = sys.stdin.readline

def factorial(n) :
    result = 1
    for i in range(1,n+1) :
        result *= i

    return result

# 조합 N C M 경우의 수 출력
# N! / M!(N-M)!
T = int(input()) # test case
answer = []
for i in range(T) :
    N, M = map(int, input().split())
    print(M,"! //",N,"! *",M-N,"!")
    answer.append(factorial(M) // (factorial(N)*factorial(M-N) ))

for a in answer:
    print(a)

