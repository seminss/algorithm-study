'''
k 초마다 손님 한명와서 줄을 선다.
음료 한번에 하나씩 만든다. 
0번 음료 : 5초
1번 음료 : 12초
2번 음료 : 30초
'''
from collections import deque

def solution(menu, order, k):
    order_list = []
    current = []
    
    # order_list [0, 5, 12]
    # current [1, 2, 2, 3]
    
    for i in range(len(order)) :
        order_list.append(menu[order[i]])
        current.append(len(order_list))
        order_list[0] = order_list[0] - k
        
        while order_list and order_list[0] <= 0:
            if len(order_list) >= 2 :
                order_list[1] += order_list[0]
            order_list.pop(0)
    
    answer = max(current)
    return answer