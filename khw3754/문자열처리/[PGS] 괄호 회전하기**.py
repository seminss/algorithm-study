# 짝인지 확인해주는 함수
def is_pair(a, b):
    if (a, b) in [('[', ']'), ('{', '}'), ('(', ')')]:
        return True
    else:
        return False


# 올바른 괄호 문자열인지 확인해주는 함수
def check(s):
    stack = []
    for i in s:
        # 비어있으면 추가
        if not stack:
            stack.append(i)
        # 짝이면 pop
        elif is_pair(stack[-1], i):
            stack.pop()
        # 아니면 추가
        else:
            stack.append(i)

    if stack:
        return False
    else:
        return True


def solution(s):
    answer = 0

    for i in range(len(s)):
        if check(s):
            answer += 1
        s = s[1:] + s[0]

    return answer