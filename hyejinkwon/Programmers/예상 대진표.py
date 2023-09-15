# 4번 -> 3번 짝수면 n-1
# 7번 -> 8번 홀수면 n+1

# 4번 vs 3번   7번 vs 8번 무조건 이긴다고 가정.
# 2번 vs 1번   4번 vs 3번 무조건 이긴다고 가정.
# 1번          2번 --> return 3

def solution(n,a,b):
    answer = 0
    
    while a != b :
        answer += 1
        a, b = (a+1)//2, (b+1)//2
        
    return answer