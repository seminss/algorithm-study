# 최대한 많이 탐험

from itertools import permutations

def solution(k, dungeons):
    answer = -1
    possible = []
    advanture_list = [i for i in range(len(dungeons))]
    combi = list(permutations(advanture_list,len(dungeons)))

    
    for c in combi :

        blood = k
        count = 0
        for i in range(len(dungeons)) :
        
            if blood < dungeons[c[i]][0] :
                break
            else :
                blood -= dungeons[c[i]][1]
                count += 1
        possible.append(count)

    answer = max(possible)
    
    return answer