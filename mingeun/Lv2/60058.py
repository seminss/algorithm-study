'''2023.7.11
-1
u가 올바른 문자열이 아닌 경우 '('(u[0]) + solution(v) + ')'(u[-1]) + u[1:-1] 괄호 뒤집음
'''

OPEN, CLOSE = '(', ')'


def isbalanced(s:str)->bool:
    cnt = 0
    for c in s:
        if c == OPEN:
            cnt += 1
        elif c == CLOSE:
            cnt -= 1
    return cnt == 0


def divide(s:str)->[str, str]:
    s1,s2 = '', ''
    for i in range(len(s)):
        s1 += s[i]
        if isbalanced(s1):
            for j in range(i+1, len(s)):
                s2 += s[j]
            return [s1, s2]
    
    
def iscorrect(s:str)->bool:
    stack = []
    for c in s:
        if c == OPEN:
            stack.append(c)
        elif c == CLOSE:
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    return True
    
    
def solution(p):
    answer = ''
    if iscorrect(p):
        answer = p
    else:
        u, v = divide(p)
        # u가 올바른 괄호 문자열 
        if iscorrect(u):
            answer = u + solution(v)
        # u가 올바른 괄호 문자열이 아님
        else:
            answer += OPEN + solution(v) + CLOSE
            for c in u[1:-1]:
                if c == OPEN:
                    answer += CLOSE
                else:
                    answer += OPEN
    return answer
