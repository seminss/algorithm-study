# 각반 대표 1명 한학생당 최대 한개의 종목대표만 가능
# 각 반의 종목 대표 능력치 합 최대화하기

def DFS(L,V, ability, visited) :
    global answer
    
    student = len(ability)
    subject = len(ability[0])

    if L == subject :
        answer = max(answer, V)
        
    else :
        for i in range(student) :
            if visited[i] == False :
                visited[i] = True
                DFS(L+1, V+ability[i][L], ability, visited)
                visited[i] = False

def solution(ability):
    global answer 
    answer = 0
    student = len(ability)
    subject = len(ability[0])
    visited = [False]*student
    
    DFS(0, 0, ability,visited)
    
    return answer