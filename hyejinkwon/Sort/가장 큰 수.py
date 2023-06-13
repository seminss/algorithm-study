# 최대 numbers는 1000 -> 3자리로 비교 *3

def solution(numbers):
    answer = ''
    test = []
    for n in numbers : 
        test.append(str(n))
        
    test = sorted(test, key = lambda x : x*3, reverse=True)
    answer = str(int(''.join(test)))
    
    return answer