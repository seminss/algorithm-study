'''
def solution(elements):
    answer = 0
    sum_set = set()
    
    # elements를 2배로 만들어줌
    elements *= 2

    for i in range(len(elements)//2) :
        for j in range(len(elements)//2) :
            sum_set.add(sum(elements[j:i+j+1]))
                    
    answer = len(sum_set)
    return answer
'''

def solution(elements):
    answer = 0
    sum_set = set()
    sum_set.update(elements)

    for i in range(len(elements)) :
        sum_value = elements[i]
        
        for j in range(i+1, i+len(elements)) :
            sum_value += elements[ j%len(elements) ]
            sum_set.add(sum_value)
            
    answer = len(sum_set)   
    return answer