from collections import Counter

def solution(want, number, discount):
    answer = 0
    want_dict = {}
    for i,w in enumerate(want) : 
        want_dict[w] = number[i]
    
    for i in range(len(discount)-9) :
        dis_dict = dict(Counter(discount[i:i+10]))

        if dis_dict == want_dict :
            answer +=1
    
    return answer
    
