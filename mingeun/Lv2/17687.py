''' 2023.5.7
17:23 ~ 17:47

0 1  2  3  4   5   6   7   8
0 01 10 11 100 101 110 111 1000
'''

def d2c(d):
    chars = '0123456789ABCDEF'
    return chars[d%16]

def radix_n(n:int , decimal:int) -> int:
    result = []
    while decimal >= n:
        result.append(d2c(decimal%n))
        decimal = decimal//n
    result.append(d2c(decimal))
    return ''.join(result[::-1])
    
def solution(n, t, m, p):
    """
    n: 진법, t: 미리 구할 숫자 개수, m: 게임에 참가하는 인원, p: 튜브 순서
    """
    answer = ''
    # 게임 시작
    target_number = 0 # 말해야 하는 숫자(10진법)
    current_player = 0
    while True:
        target_str = (radix_n(n, target_number))  
        # current_player부터 차례대로 말한다.
        for i, c in enumerate(target_str):
            if current_player == p - 1:
                answer += c
                if len(answer) == t:
                    return answer
            current_player = (current_player+1)%m
        target_number += 1
    return answer
