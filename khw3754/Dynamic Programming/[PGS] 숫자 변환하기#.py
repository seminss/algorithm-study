from collections import deque
def solution(x, y, n):
    q = deque()
    result = [-1] * (y + 1)
    result[x] = 0
    q.append(x)
    while q:
        num = q.popleft()
        d = [num + n, num * 2, num * 3]
        for n_num in d:
            if n_num > y:
                continue
            if result[n_num] == -1:
                result[n_num] = result[num] + 1
                q.append(n_num)
            elif result[n_num] > result[num] + 1:
                result[n_num] = result[num] + 1
                q.append(n_num)

    return result[y]