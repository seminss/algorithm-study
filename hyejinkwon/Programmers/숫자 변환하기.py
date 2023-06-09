# x <= y 가 되는 모든 연산결과를 set에 저장

def solution(x, y, n):
    answer = 0
    result = False
    result_set = set()
    result_set.add(x)

    while result_set :
        if y in result_set :
            result = True
            break
            
        test_set = set()
        for s in result_set :
            if s+n <= y :
                test_set.add(s+n)
            if s*2 <= y :
                test_set.add(s*2)
            if s*3 <= y :
                test_set.add(s*3)
        
        result_set = test_set
        answer += 1
        
    if not result:
        return -1
    
    return answer