def GCD(N1, N2) :
    while N2 > 0 :
        N1, N2 = N2, N1%N2
    
    return N1

def LCM(N1,N2) :
    gcd = GCD(N1,N2)
    return N1*N2//gcd

def solution(arr):
    answer = 0
    i = 0
    before_lcm = LCM(arr[i], arr[i+1])
    i = 2
    
    while i < len(arr) :
        lcm = LCM(before_lcm, arr[i])
        before_lcm = lcm
        i+=1
        
    answer = before_lcm
    return answer