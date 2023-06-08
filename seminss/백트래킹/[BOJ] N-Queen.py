import sys
from array import array

n = int(sys.stdin.readline())
col = array('i', [0] * (n + 1))

def promising(i):
    for j in range(1, i):
        if col[j] == col[i] or abs(col[i] - col[j]) == i - j:
            return False
    return True

def queens(i):
    if i == n:
        return 1
    count = 0
    for j in range(1, n + 1):
        col[i + 1] = j
        if promising(i + 1):
            count += queens(i + 1)
    return count

answer = queens(0)
print(answer)

# answer을 global로 선언하는 대신 반환값으로 수정
# 리스트를 array로 수정
# python 대신 pypy로 실행