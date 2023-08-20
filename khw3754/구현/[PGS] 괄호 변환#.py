# 올바른 괄호 문자열 체크
def check(s):
    stack = []
    for i in s:
        stack.append(i)
        if len(stack) > 1 and stack[-2] == '(' and stack[-1] == ')':
            stack.pop()
            stack.pop()
    if stack:
        return False
    else:
        return True


# u, v로 분리, 반환
def split_p(p):
    count_9 = 0
    count_0 = 0
    result = ''
    for i in p:
        if i == '(':
            count_9 += 1
            result += i
        elif i == ')':
            count_0 += 1
            result += i

        if count_9 == count_0:
            return result, p[len(result):]


def rec(p):
    if not p:
        return ''

    # 2
    u, v = split_p(p)
    # 3
    if check(u):
        r = rec(v)
        return u + r
    # 4
    else:
        result = '('
        result += rec(v) + ')'
        u = u[1:-1]
        for i in u:
            if i == '(':
                result += ')'
            else:
                result += '('
        return result


def solution(p):
    if not p:
        return ''

    if check(p):
        return p

    return rec(p)