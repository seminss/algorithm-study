#패션왕 신해빈
import sys
T=int(sys.stdin.readline()) #Testcase

for i in range(T):
    hashmap={}
    n=int(sys.stdin.readline()) #옷 개수

    for j in range(n):
        detail,category=map(str,sys.stdin.readline().strip().split())
        if category not in hashmap:
            hashmap[category]=[detail] #categry:key(카테고리), detail:value(옷 종류) 리스트로 저장
        else:
            hashmap[category].append(detail)

    mixmatch=1
    for k,v in hashmap.items():
        mixmatch*=(len(v)+1) #해당 의상 착용 하지 않는 경우 포함(+1)
    mixmatch-=1 #알몸 상태 빼주기

    print(mixmatch)