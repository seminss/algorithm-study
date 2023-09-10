def solution(n, left, right):
    answer = []
    ln = left // n
    lnn = left % n
    rn = right // n
    rnn = right % n

    for row in range(ln, rn + 1):
        arr = [(row + 1)] * (row + 1)
        ext = [i for i in range(row + 2, n + 1)]
        arr.extend(ext)

        ### 문제: 하나의 열에서 가져오는 경우 처리가 안됐음
        if ln == rn:
            answer.extend(arr[lnn:rnn + 1])
        elif row == ln:
            answer.extend(arr[lnn:])
        elif row == rn:
            answer.extend(arr[:rnn + 1])
        else:
            answer.extend(arr)

    return answer

# 시간초과
# def solution(n, left, right):
#     arr2 = [[0] * n for _ in range(n)]
#     for i in range(n):
#         for j in range(n):
#             arr2[i][j] = max(i+1, j+1)
#     print(arr2)
#     arr = []
#     for a in arr2:
#         for i in a:
#             arr.append(i)

#     return arr[left:right+1]