# DP

def solution(sticker):
    answer = 0
    
    if len(sticker) == 1:
        return sticker[0]
    
    
    pan = [0 for _ in range(len(sticker))]
    # 0번 스티커 -> 맨마지막 x
    pan[0] = sticker[0]
    pan[1] = pan[0]
    
    for i in range(2, len(sticker)-1) :
        pan[i] = max(pan[i-1], pan[i-2]+sticker[i])
    
    answer = max(pan)
    
    # 1번 스티커 -> 맨마지막 o
    pan = [0 for _ in range(len(sticker))]
    pan[0] = 0
    pan[1] = sticker[1]
    for i in range(2, len(sticker)) :
        pan[i] = max(pan[i-1], pan[i-2]+sticker[i])
        
    answer = max(answer, *pan)
    '''
    
    pan = [[0 for _ in range(len(sticker))]for _ in range(2)]
    pan[0][0] = sticker[0]
    pan[0][1] = pan[0][0]
    pan[1][0] = 0
    pan[1][1] = sticker[1]
    
    for i in range(2, len(sticker)-1) :
        pan[0][i] = max(pan[0][i-1], pan[0][i-2]+sticker[i])
    for i in range(2, len(sticker)) :
        pan[1][i] = max(pan[1][i-1], pan[1][i-2]+sticker[i])
    
    answer = max(*pan[0], *pan[1])
    '''
    return answer