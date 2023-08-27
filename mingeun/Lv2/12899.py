def solution(n):
    """
    3진법에서 0대신 4 사용
    """
    answer = []
    while n > 0:
        if n%3 == 0:
            answer.append(str('4'))
            n = (n//3)-1
        else:
            answer.append(str(n%3))
            n//=3
    return ''.join(answer[::-1])
