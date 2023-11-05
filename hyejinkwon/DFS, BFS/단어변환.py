from collections import deque

def solution(begin, target, words):
    answer = 0
    visited = [False]*len(words)
    
    if target not in words : return 0

    queue = deque()
    queue.append([begin,0])
    
    while queue :
        ww, stage = queue.popleft()
        
        if ww == target :
            answer = stage
            break
        
        for i in range(len(words)) :
            dif = 0
            if not visited[i] :
                for j in range(len(ww)) :
                    if ww[j] != words[i][j] :
                        dif += 1
                if dif == 1 :
                    queue.append([words[i], stage+1])
                    visited[i] = True
    
    return answer