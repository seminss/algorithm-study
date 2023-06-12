import sys
input = sys.stdin.readline

N = int(input())
length = list(map(int, input().split()))
pay = list(map(int, input().split()))

# 최소 리터당 주유 가격 : 첫 도시의 리터당 주유 가격으로 초기화 
answer = 0
before_pay = pay[0]

# 마지막 지역의 기름 살 수 없음
for i in range(N-1) :
    if before_pay > pay[i] :
        before_pay = pay[i]
    answer += length[i]*before_pay
    
print(answer)