def solution(numbers):
    answer = [-1] * len(numbers)

    # (숫자, 인덱스)로 스택에 저장
    stack = []
    for idx, num in enumerate(numbers):
        if not stack:
            stack.append((num, idx))
            continue

        if stack[-1][0] >= num:
            stack.append((num, idx))

        else:
            while stack and stack[-1][0] < num:
                n, i = stack.pop()
                answer[i] = num
            stack.append((num, idx))

    return answer