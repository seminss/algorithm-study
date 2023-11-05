#7:40~8:38
from collections import defaultdict
from itertools import combinations

def solution(orders, course):
    answer = []
    orders.sort(key=lambda x:len(x))
    list_=list(set(c for c in o) for o in orders)
    
    for k in course: #첫번째 루프를 course로 하면 combi 수를 줄일 수 있다.
        dict=defaultdict(int)
        for o in list_:
            combi=list(combinations(o,k))
            for c in combi:
                tmp="".join(sorted(list(c)))
                dict[tmp]+=1
        for k,v in dict.items():
            if v==max(dict.values()) and v>=2:
                answer.append(k)
    return sorted(answer)