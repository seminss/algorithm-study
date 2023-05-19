# 가격이 떨어지지 않은 기간 : 몇 초

def solution(prices):
    answer = []
    
    for i in range(len(prices)) :
        test = 0
        for j in range(i+1, len(prices)) :
            if prices[i] > prices[j] :
                test += 1
                break
            test += 1
        answer.append(test)
    
    return answer

# 효율성 테스트 최대 158ms