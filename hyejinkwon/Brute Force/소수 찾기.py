from itertools import permutations

def is_prime(n) :
    for i in range(2,int(n**0.5)+1) :
        if n % i == 0 :
            return False
    return True

def solution(numbers):
    answer = 0
    str_list = []
    test = []
    int_set = set() # 중복되는 수 걸러내기 위해 set 사용
    
    for n in numbers :
        str_list.append(n)
        
    for i in range(1,len(numbers)+1) :
        test.append(list(permutations(str_list,i)))
    
    for t in test :
        for t_i in t :
            int_set.add(int(''.join(t_i)))
    
    print(int_set)
    for n in int_set :
        if n > 1 and is_prime(n) :
            answer += 1
    
    return answer