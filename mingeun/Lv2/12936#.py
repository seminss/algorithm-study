'''2023.7.16
-1
'''
from math import factorial
def solution(n, k):
    numbers = [i for i in range(1, n+1)]
    answer = []
    k = k - 1
    for i in range(n):
        if i == n - 1:
            x = numbers[0]
        else:
            x = numbers[k//factorial(n-i-1)]
            k = k % factorial(n-i-1)
        answer.append(x)
        numbers.remove(x)
    return answer
