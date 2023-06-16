def solution(number, k):
    answer = ''
    stack = [] # stack 이용
    stack.append(number[0]) # 초기값 append
    
    for i in range(1,len(number)) :        
        if k > 0 :
            while stack[-1] < number[i]: # stack의 마지막 값이 더 작다면 pop
                stack.pop()              # -> 가장 큰 수를 만들기 위해 
                k -= 1 # 원하는 개수만큼만 제거
                
                # k를 가감하는 연산 중 0보다 작거나 같아지면 / stack이 빈다면 중단
                if not stack or k <= 0 : 
                    break
                    
        stack.append(number[i])
    
    if k > 0 : # k =1 인 경우 오류처리 
        answer = ''.join(stack)[:-1]
    if k == 0 :
        answer = ''.join(stack)
        
    return answer