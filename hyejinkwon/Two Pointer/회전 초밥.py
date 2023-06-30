# 임의의 한 위치부터 k개의 접시 연속 -> 할인
# 초밥 종류 1개의 쿠폰 발행 -> 무료 제공

import sys
input = sys.stdin.readline

N, d,k,c = map(int,input().split())
sushi = []
kind = {}
kind[c] = 1 # 쿠폰번호에 해당하는 스시

L,R = 0, k-1

for _ in range(N) :
    sushi.append(int(input()))

# k만큼 개수의 구간 종류별 개수 저장
for i in range(R+1) :
    if sushi[i] in kind : 
        kind[sushi[i]] += 1
    else :
        kind[sushi[i]] = 1

answer = 0
while L < N :
    answer = max(len(kind), answer)

    kind[sushi[L]] -= 1
    if kind[sushi[L]] == 0 :
        del kind[sushi[L]]
    L+=1
    R+=1
    if sushi[R%N] in kind :
        kind[sushi[R%N]] += 1
    else :
        kind[sushi[R%N]] = 1

print(answer)

