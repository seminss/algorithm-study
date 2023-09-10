def solution(s):
    stack = [s[0]]
    for i in s[1:]:
        if stack[-1:] != [i]:
            stack.append(i)
        else:
            stack.pop()

    if stack:
        return 0
    else:
        return 1