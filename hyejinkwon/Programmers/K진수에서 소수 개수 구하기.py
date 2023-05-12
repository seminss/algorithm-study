import math

def is_prime(number) :
    for i in range(2,int(math.sqrt(number)) + 1) :
        if number % i == 0 :
            return False
    else :
        return True
    

def change(number, k) :
    result = ""
    
    while number != 0 :
        result += str(number%k)
        number //= k

    return result[::-1]
        
def solution(n, k):
    answer = 0
    change_number = change(n,k)
    result = ""
    test_list = []
    
    for c in change_number :
        if c != '0' :
            result += c
        else :
            if result != "" :
                test_list.append(result)
            
            result = ""
            
    if result != "" :
        test_list.append(result)
        
    for t in test_list :
        if int(t) > 1 and is_prime(int(t)) :
            answer += 1
            
    return answer