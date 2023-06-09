def solution(arr):
    # 0의 개수, 1의 개수
    answer = [0,0]    
    n = len(arr)
    
    # quard 영역 내 같은 수가 되는지 확인
    def quard(x,y,n) :
        number = arr[x][y] 

        for i in range(x,x+n) :
            for j in range(y,y+n) :
                if number != arr[i][j] : # 하나라도 영역 내 다른 수가 있다면
                    n //= 2 # 영역 나누기 절반씩 
                    quard(x,y,n)
                    quard(x+n,y,n)
                    quard(x,y+n,n)
                    quard(x+n,y+n,n)
                    return 

        # 0의 개수인지 1의 개수인지 판별 
        answer[number] += 1
        return answer
    
    quard(0,0,n)
    
    return answer