# 최소 2가지 이상의 단품메뉴로 구성
# 최소 2명 이상의 손님으로부터 주문된 단품메뉴 조합

from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    orders = sorted(orders, key = lambda x :len(x))
    candidate = []

    for c in course : 
        string_list = []
        for o in orders : 
            string_list += combinations(sorted(o),c)
            
        counter_list = Counter(string_list).most_common()
        
        for word, count in counter_list :
            if count == counter_list[0][1] and count >= 2 :
                answer.append(''.join(word))
                
    answer.sort(reverse=False)
    return answer