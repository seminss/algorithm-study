# 같은 알파벳 2개 붙어 있는 짝 찾기
# 그 둘 제거
# 앞뒤 문자열 이어 붙이기
# -> 무한반복 문자열 모두 제거 : 종료
# 성공 1 실패 0

def solution(s):
    # 스택 !
    stack = []
    for ss in s :
        if ss not in stack:
            stack.append(ss)
        else : # 이미 존재
            if ss == stack[-1] :
                stack.pop()
            else :
                stack.append(ss)
            
    if stack == [] :
        return 1
    else :
        return 0
    
    return answer