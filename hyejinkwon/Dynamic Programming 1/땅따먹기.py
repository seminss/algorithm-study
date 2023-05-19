# N행 4열의 땅
# 한 행씩 내려올 때 같은 열을 연속해서 밟을 수 없는 특수 규칙이 있음

def solution(land):
    answer = 0
    
    for i in range(1, len(land)) :
        for j in range(4) :
            land[i][j] += max(land[i-1][:j] + land[i-1][j+1:])

    answer = max(land[len(land)-1])
            
    return answer