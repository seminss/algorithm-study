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
    
    for n in numbers :
        str_list.append(n)
    
    for i in range(1,len(numbers)+1) :
        # permutations 순열 사용후 list를 연결해주는
        # append 보다 += 를 선호
        test += list(permutations(str_list,i))
        
    # 중복되는 수 걸러내기 위해 set 사용
    int_set = set(int(("").join(p)) for p in test)
        
    '''
    for t in test :
        for t_i in t :
            int_set.add(int(''.join(t_i)))
    
    '''
    
    for n in int_set :
        if n > 1 and is_prime(n) :
            answer += 1
    
    return answer