'''
2023.5.5
14:32 ~ 15:22
2023.5.7
00:55 ~ 01:00 시간초과
07:43 ~ 8:19
'''
def simulate(d:int, tobuy: dict, discount: list, want: list) -> bool:
    _tobuy = dict(tobuy)
    cnt = 0
    for i in range(d, d+10):
        product = discount[i]
        if product in _tobuy and _tobuy[product] > 0:
            _tobuy[product] -= 1
            if _tobuy[product] == 0:
                cnt += 1
                if cnt == len(want):
                    return True
        else:
            return False
    return False
        
    
def solution(want, number, discount):
    answer = 0
    tobuy = dict()
    # 사야할 목록 {품목: 개수}
    for i in range(len(number)):
        tobuy[want[i]] = number[i]
    for d in range(len(discount)-9):
        if simulate(d, tobuy, discount, want):
            answer += 1
    return answer
