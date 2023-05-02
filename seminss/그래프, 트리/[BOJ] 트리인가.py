import sys

# 들어오는 간선이 하나도 없는 단 하나의 노드 : root 노드
# 만약 들어오는 간선이 하나도 없는 노드를 찾았는데 root가 이미 있으면, case를  false로 종료한다.
# 만약 들어오는 간선이 하나도 없는 노드가 없으면, case를 false로 종료
# 루트 노드로 들어오는 간선이 존재하면 case는 false
# 루트에서 다른 노드로 가는 경ㅇ로는 반드시 존재, 유일
def isTree(tree):
    print(tree)
    return True

case=1
while True:
    data=[]
    while True:
        d=sys.stdin.readline().strip()
        data+=list(map(int,d.split()))
        if len(data)>0 and data[-1]<0 and data[-2]<0:
            exit()
        if '0 0' in d:
            data.pop()
            data.pop()
            break
    if len(data)==0:
        print('case {0} is a tree'.format(case)) #0 0 밖에 없는 경우
    else:
        tree={}
        for i in range(0,len(data),2):
            u,v=data[i],data[i+1]
            if u in tree:
                tree[u].append(v)
            else:
                tree[u]=[v]
        if isTree(tree): 
            #처음에 여기서 len(v.values())==len(set(v.values()))로 검사했더니 문제 조건 전부 충족 x
            #그래서 isTree함수를 만들어 여러 조건을 전부 확인해보기로 했다.
            print('case {0} is a tree'.format(case))
        else:
            print('case {0} is not a tree'.format(case))
    case+=1