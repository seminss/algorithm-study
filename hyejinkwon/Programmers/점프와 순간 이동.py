def solution(n):
    ans = 0
    
    while n != 0 :
        # 홀수칸일 때는 점프 짝수칸일 때는 순간이동
        ans += n%2
        n //= 2
    
    return ans