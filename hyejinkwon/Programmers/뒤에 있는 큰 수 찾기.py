# 자신보다 크면서 가장 가까이 있는 수 : 뒷 큰수
# 마지막 원소는 항상 -1 반환
# 이중 for문 X -> 시간초과
# stack 이용 O
        
def solution(numbers):
    answer = [-1] * len(numbers)
    num_stack = []
    
    for i,n in enumerate(numbers) :
        # print(i,"번째 숫자 :",n,"stack : ",num_stack)
        while num_stack and n > numbers[num_stack[-1]] :
                answer[num_stack[-1]] = n
                num_stack.pop()
        num_stack.append(i)
        
    return answer