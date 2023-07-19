'''2023.7.19
22:30 ~ 23:25
'''
import math
def solution(k, d):
    """
    그냥 모든 x좌표에 대해 최대 y좌표를 구하면 되는 문제
    """
    answer = 0
    for x in range(d+1):
        if x % k == 0:
            y = int(math.sqrt(d*d - x*x))
            answer += (y//k + 1)
    return answer
