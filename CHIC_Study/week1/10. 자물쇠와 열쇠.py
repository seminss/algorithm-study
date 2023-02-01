# https://school.programmers.co.kr/learn/courses/30/lessons/60059

def lotate_90(arr): #2차원 리스트 90도 회전
    n=len(arr) #행 길이
    m=len(arr[0]) #열 길이, 정사각 형태의 격자니까 사실 n=m 이긴 함
    res=[[0]*n for _ in range(m)] #회전된 결과 저장할 list, 행->열, 열->행
    for i in range(n):
        for j in range(m):
            res[j][n-i-1] = arr[i][j]
    return res

def check(new_lock): #값을 더한 자물쇠의 중간 부분이 모두 1인지 확인
    lock_len=len(new_lock)//3 
    for i in range(lock_len,lock_len*2):
        for j in range(lock_len,lock_len*2):
            if new_lock[i][j]!=1:
                return False
    return True

def solution(key, lock):
    n=len(lock) #자물쇠
    m=len(key) #키

    #자물쇠 크기를 기존 3배로 변환, 0 초기화
    new_lock=[[0]*(n*3) for _ in range(n*3)]

    #새로운 자물쇠의 중앙 부분에 기존의 자물쇠를 넣는다.
    for i in range(n):
        for j in range(n):
            new_lock[n+i][n+j]=lock[i][j]

    for rotation in range(4): #90,180,270,360(0)
        key=lotate_90(key)
        for x in range(n*2):
            for y in range(n*2):
                #자물쇠에 열쇠 값을 더하기
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] += key[i][j]
                if check(new_lock)==True:
                    return True #성공
                #자물쇠에서 열쇠를 다시 빼기
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j]-=key[i][j]

    return False #rotation 다 돌 때까지 성공을 못했니?