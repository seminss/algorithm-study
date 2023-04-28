# 4번 -> 3번 짝수면 n-1
# 7번 -> 8번 홀수면 n+1

# 4번    7번
# 4번 vs 3번   7번 vs 8번
# 2번          4번
# 2번 vs 1번   4번 vs 3번
# 1번          2번

def solution(n,a,b):
    answer = 0
    now = [a,b]
    fight_a = [a]
    fight_b = [b]
    round = 2
    
    # 초기 값 설정
    if a%2 == 0 :
        fight_a.append(a-1)
    else :
        fight_a.append(a+1)
        
    if b%2 == 0 :
        fight_b.append(b-1)
    else :
        fight_b.append(b+1)
        
    if fight_a[0] in now and fight_a[1] in now :
        return 1
    if fight_b[0] in now and fight_b[1] in now :
        return 2
        
    while fight_a != now and fight_b != now :
        now = [fight_a[1]//2 if fight_a[1]%2 ==0 else fight_a[1]//2+1, fight_b[1]//2 if fight_b[1]%2 ==0 else fight_b[1]//2+1]
        
        fight_a = [now[0], now[0]-1 if now[0]%2 ==0 else now[0]+1 ]
        if fight_a[0] in now and fight_a[1] in now :
            break
        
        fight_b = [now[1], now[1]-1 if now[1]%2 ==0 else now[1]+1 ]
        round += 1

        if fight_b == now :
            print(fight_b,now)
            break
        
    answer = round

    return answer