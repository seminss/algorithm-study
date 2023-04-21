import sys 

input = sys.stdin.readline

def isPrimeNum(N) :
    for i in range(2, N) :
        if N%i == 0 :
            return False
    else :
        return True

N = int(input())
N_list = list(map(int, input().split()))
count = 0

for n in N_list :
    if n == 1 :
        continue 
    if isPrimeNum(n) :
        count += 1

print(count)