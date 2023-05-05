def solution(elements):
    answer = 0
    sum_set = set()
    
    # 내 풀이
    # 0~len(elements)
    # len(elements) 넘어가면 len(elements)%index

    # elements를 2배로 만들어줌
    elements *= 2

    for i in range(len(elements)//2) :
        for j in range(len(elements)//2) :
            sum_set.add(sum(elements[j:i+j+1]))
                    
    answer = len(sum_set)
    return answer