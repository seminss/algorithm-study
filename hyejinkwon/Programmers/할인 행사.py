# 10일 연속으로 일치할 경우 회원가입
# extend

def solution(want, number, discount):
    answer = 0
    possible_buy = []
    want_list = []
    
    for i in range(len(want)) :
        want_list.extend([want[i]]*number[i])
    
    for i in range(len(discount)-9) :
        possible_buy = discount[i:i+10]

        if sorted(possible_buy) == sorted(want_list) :
            answer += 1
            
    return answer
    
