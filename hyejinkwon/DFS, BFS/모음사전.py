from itertools import product

def solution(word):
    answer = 0
    
    words = 'AEIOU'
    words_list = []
    
    def dfs(count, w) :
        
        if count == 5 :
            return 
        else :
            for i in words :
                words_list.append(w+i)
                dfs(count+1, w+i)
        
        return words_list
    
    answer = dfs(0,"").index(word) + 1
    
    return answer