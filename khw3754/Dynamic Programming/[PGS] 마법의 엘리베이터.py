# 일의 자리부터 하나씩 진행
def solution(storey):
    answer = 0

    step = 10
    while storey != 0:
        target = storey % step
        if target == 0:
            storey //= 10
        ######## 이게 문제 ############
        elif target == 5 and storey % 100 >= 55:
            answer += 5
            storey = storey // 10 + 1
        elif target <= 5:
            answer += target
            storey //= 10
        else:
            answer += 10 - target
            storey = storey // 10 + 1

    return answer