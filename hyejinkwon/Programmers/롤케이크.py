# 각 조각에 동일한 가짓수의 토핑이 올라가면 공평하다
# 완탐..?
# 토핑 종류 수는 set으로 처리할 예정 -> X

# Counter 라이브러리 이용 1개씩 빼고
# set에는 1개씩 추가하여 둘의 개수 비교 

from collections import Counter

def solution(topping):
    answer = 0
    counter = Counter(topping)
    set_counter = set()
    
    for t in topping :
        counter[t] -= 1
        set_counter.add(t)
            
        if counter[t] == 0 : # 더 이상 해당되는 토핑이 없으면 
            counter.pop(t)
        
        if len(counter) == len(set_counter) :
            answer += 1
            
    return answer