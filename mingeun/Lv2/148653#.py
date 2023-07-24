'''2023.7.22
-1
'''
def solution(storey):
    answer = 0
    c = 10
    while storey > 0:
        n = storey % c
        storey //= c
        # 올림
        print(n, end=' ')
        if n > 5:
            answer += (10 - n)
            print(10 - n)
            storey += 1
        # 버림
        elif n < 5:
            answer += n
            print(-n)
        # 앞 자리의 수에 따라 결정
        elif n == 5:
            answer += n
            # 0, 1, 2, 3, 4인 경우 버리고 4보다 큰 경우 올린다.
            if storey % c > 4:
                storey +=1
    return answer

