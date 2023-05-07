''' 2023.5.7
14:47 ~ 16:04
'''
answer = 0
def done(e, visited, dungeons) -> bool:
    result = True # 탐험 가능한 던전이 하나라도 있으면 False
    for i in range(len(dungeons)):
        if i not in visited:
            if e >= dungeons[i][0]:
                result = False
    return result
    
def dfs(e:int, start:int , visited:list, dungeons:list) -> None:
    """
    순열 구현
    중간에 조건을 만족하지 않으면 탐색하지 않는다.
    e: 현재 피로도
    """
    global answer
    # 모든 던전을 탐험했거나 더 이상 탐험할 던전이 없는 경우
    if done(e, visited, dungeons):
        answer = max(answer, len(visited))
        return
    else:
        for i in range(len(dungeons)):
            if i not in visited and e >= dungeons[i][0] and e-dungeons[i][1]>=0:
                visited.append(i)
                dfs(e-dungeons[i][1], i, visited, dungeons)
                visited.pop()
    
def solution(k, dungeons):
    dfs(k, 0, [], dungeons)
    return answer
