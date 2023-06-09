# 다음과 같이 import를 사용할 수 있습니다.
# import math

def solution(garden):
    # 여기에 코드를 작성해주세요.
    answer = 0
    visited = []
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    while len(visited) < len(garden)**2:
        
        visited.clear()
        for i in range(len(garden)) :
            for j in range(len(garden)) :
                if garden[i][j] == 1 :
                    visited.append([i,j])
        
        for x,y in visited :
            for k in range(4) :
                xx = x + dx[k]
                yy = y + dy[k]
            
                if 0<= xx <len(garden) and 0<= yy<len(garden) :
                    garden[xx][yy] = 1
                
        answer += 1
            
    return answer-1 

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
garden1 = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
ret1 = solution(garden1)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

garden2 = [[1, 1], [1, 1]]
ret2 = solution(garden2)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")