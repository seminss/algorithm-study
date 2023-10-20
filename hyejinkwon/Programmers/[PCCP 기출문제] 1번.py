'''
1초마다 x 체력 회복
t초 연속으로 붕대 감기 성공 -> y만큼 체력 회복
공격 당하고 기술 끝나면 붕대감기 다시~ 연속성공시간 0초
현재 체력 <= 0, 죽어



'''

def solution(bandage, health, attacks):
    answer = 0
    max_health = health # 최대 체력
    attack_index = 0
    con = 0
    gameout = False
    
    for i in range(1, attacks[len(attacks)-1][0] + 1) :
        att = False
        
        if i == attacks[attack_index][0] :
            health -= attacks[attack_index][1]
            attack_index += 1
            con = 0
            att = True

            if health <= 0 :
                gameout = True
                break
            
        if not att and health < max_health : 
            health += bandage[1]
            con += 1
            if health > max_health : health = max_health
            
        elif not att and health == max_health :
            con += 1
            
        if not att and con == bandage[0] : 
            con = 0
            health += bandage[2]
            if health > max_health : health = max_health
        
    if gameout : return -1
    answer = health            
    return answer