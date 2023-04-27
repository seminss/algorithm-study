def solution(n):
    ans = 0

    # n을 계속 2로 나누는데, 홀수일 때 1칸 점프가 필요
    # ex) n=21 : 21-20,10,5-4,2,1-0  --> 1칸씩 3번 점프.

    while n != 0:
        if n % 2 != 0:
            ans += 1
            n -= 1
        else:
            n = n // 2

    return ans