# 택배 기사님이 알려준 순서에 맞게 택배상자를 실자
# 순서가 아니면 택배 잠시 다른 곳에 보관 -> "보조컨테이너" 맨앞의 상자만 꺼낼 수 있음
# "보조컨테이너" -> stack
# 보조컨테이너 써도 원하는 순서아니라면 더이상 상자 싣지 않음

# 컨테이너 4 3 1 2 5
# 1 2 3 -> 보조 컨테이너
# 4 싣고 3 싣고 끝.

def solution(order):
    answer = 0
    N = len(order)
    sub_container = [] # stack
    order_index = 0
    box = 1
    
    while box != N+1 :
        # 순서가 맞지 않는다면 sub container
        sub_container.append(box)
        
        while sub_container[-1] == order[order_index] :
            # 보조 컨테이너 맨끝과 순서 일치하면
            answer += 1
            order_index += 1
            sub_container.pop()
            
            if sub_container == [] :
                break
        
        box += 1  
    
    return answer