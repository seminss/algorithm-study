# 괄호 회전하기
# https://school.programmers.co.kr/learn/courses/30/lessons/76502#

from collections import deque

def is_ok(s):
    stack = []
    bracket = {')':'(', ']':'[', '}':'{'}
    for c in s:
        if c in bracket.values():
            stack.append(c)
        elif c in bracket:
            if len(stack) == 0 or stack[-1] != bracket[c]:
                return False
            elif stack[-1] == bracket[c]:
                stack.pop()
    # 스택이 비어있어야 모든 괄호가 짝지어진 경우이다.
    if len(stack) > 0:
        return False
    return True


def solution(s):
    answer = 0
    q = deque(s)
    for i in range(len(s)):
        if is_ok(q):
            answer += 1
        q.append(q.popleft())
    return answer
