# 최대공약수 주의!
def GCD(a,b) :
    while b > 0 :
        a, b = b, a%b
        
    return a
    
def LCM(a,b, gcd) :
    return gcd * a//gcd * b//gcd
    
    
def solution(arr):
    answer = 0
    
    for i in range(1,len(arr)) :
        gcd = GCD(arr[i-1], arr[i])
        print(arr[i-1], arr[i], gcd)
        lcm = LCM(arr[i-1], arr[i], gcd)
        arr[i] = lcm
        
    answer = arr[-1]
    
    return answer