from itertools import product

def solution(word):
    answer = 0
    words = []
    
    
    for i in range(1, 6) : 
        for p in list(product(["A","E","I","O","U"],repeat = i)) :
            words.append("".join(p))
        
    words.sort()
    answer = words.index(word) + 1
    
    return answer