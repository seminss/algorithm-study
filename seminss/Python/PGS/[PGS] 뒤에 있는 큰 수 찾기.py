def solution(numbers):
    answer = [-1]*len(numbers)
    stack=[]
    for i in range(len(numbers)):
        while stack and numbers[stack[-1]]<numbers[i]:
            answer[stack.pop()]=numbers[i]
        stack.append(i)
    return answer

#자신보다 큰 수를 찾는 문제는 스택 문제인 경우가 많다.
#스택에는 number의 인덱스 정보가 담긴다.