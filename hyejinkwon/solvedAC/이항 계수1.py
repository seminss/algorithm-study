import sys

input = sys.stdin.readline
N,K =map(int,input().split())

'''
def factorial(n) :
    if (n > 1) : return n * factorial(n-1)
    else : return 1
'''

def factorial(n) :
    result = 1
    for i in range(2,n+1) : 
        result *= i
    return result

if K == 0 or K == N :
    print(1)
else :
    print(factorial(N)//(factorial(N-K)*factorial(K)))