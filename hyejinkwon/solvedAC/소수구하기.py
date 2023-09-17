import sys
import math

input = sys.stdin.readline

N, M = map(int, input().split())

def prime_number(n) :
    for i in range(2,int(math.sqrt(n)+1)) :
        if n%i == 0 :
            return False
    else : 
        return True
    
for i in range(N,M+1) :
    if prime_number(i) :
        print(i)