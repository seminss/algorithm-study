from itertools import permutations

def eachCase(k,dungeons):
    cnt=0
    for d in dungeons:
        if k>=d[0]:
            k-=d[1]
            cnt+=1
        else:
            continue
    return cnt

def solution(k, dungeons):
    answer = -1
    mx=0
    #순서 다 다르게 순열 만들기
    dungeon_list=list(permutations(dungeons))
    for dungeons in dungeon_list:
        res=eachCase(k,dungeons)
        if mx<res: mx=res
    return mx