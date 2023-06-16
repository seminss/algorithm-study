# 임의의 두 인덱스의 원소와 그 사이의 원소를 모두 포함하는 부분 수열이어야 함
# 부분 수열의 합은 k
# 합이 k인 부분 수열이 여러 개인 경우 길이 짧은 수열 찾기
# 길이 짧은 수열이 어려개면 시작 인덱스가 작은 수열 찾기

def solution(sequence, k):
    answer = []
    sumvalue = 0
    L,R = 0, -1
    
    while True :
        if sumvalue < k :
            R += 1
            if R >= len(sequence) :
                break
            sumvalue += sequence[R]
            
        else :
            sumvalue -= sequence[L]
            if L >= len(sequence) :
                break
            L += 1
            
        if sumvalue == k :
            answer.append([L,R])
    
    answer = sorted(answer, key = lambda x : (x[1] - x[0]))
    answer = answer[0]
    
    return answer