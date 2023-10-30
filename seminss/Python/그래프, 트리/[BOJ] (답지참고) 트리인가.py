# 답지 그대로 하면 맞는데 이건 틀림,, 어떤 부분이 이상한지 모르겠네 찾아ㅇ바야할 듯
from collections import deque
import sys;rl=sys.stdin.readline

class Node():
    def __init__(self,item:int):
        self.item = item
        self.canOut = []
        self.canIn = []
        self.connectRoot = False
        
class Tree():
    def __init__(self,root:Node):
        self.root = root
    def levelorder(self,n:Node):
        if n != None:
            queue = deque()
            queue.append(n)
            while queue:
                tmp = queue.popleft()
                if tmp.connectRoot == False:
                    tmp.connectRoot = True
                    for item in tmp.canOut:
                        global nodes
                        queue.append(nodes[item])

testcase_cnt = 0

while True:
    data = dict()
    INP = rl().rstrip()
    if INP == '-1 -1': # -1 -1이 입력된 경우 입력종료
        break
    elif INP == '': # 빈 줄이 입력된 경우 무시 
        continue
    caseEnd = 0
    inputLine = list(map(int,INP.split()))
   
    for i in range(0,len(inputLine),2): 
        u,v=inputLine[i],inputLine[i+1]
        if u == 0 and v == 0:  # 입력으로 0 0이 들어올 때까지 간선 내용 저장
            caseEnd = 1
            break
        elif u in data:
            data[u].append(v)
        else:
            data[u] = [v]

    # 입력으로 0 0이 들어온 경우 case 결과 출력 후 입력 초기화
    if caseEnd == 1: 
        testcase_cnt += 1
        
        nodes = dict() # key값이 node의 item인 node dict 생성
        
        for key in data.keys(): 
            #입력 내에서 간선의 출발점이 되는 정점을 노드로 추가
            if not key in nodes.keys(): 
                nodes[key] = Node(key)
            
            for value in data[key]:
                #입력 내에서 간선의 도착점이 되는 정점을 노드로 추가
                if not value in nodes.keys(): 
                    nodes[value] = Node(value)

                #정점으로 들어오는 간선 정보를 도착정점 노드에 추가
                nodes[value].canIn.append(key) 
                #정점에서 나가는 간선 정보를 출발정점 노드에 추가
                nodes[key].canOut.append(value) 
        
        root = None
        isTree = True

        for nodeItem in nodes.keys():
            # 1. 들어오는 간선이 하나도 없는 단 하나의 노드가 존재한다. 이를 root노드라 부른다.
            if len(nodes[nodeItem].canIn) == 0:
                if root == None:
                    root = nodeItem
                # 만약 들어오는 간선이 하나도 없는 노드를 찾았는데 root가 이미 있으면, case를  false로 종료한다.
                else:
                    isTree = False
                    break
        
        # 만약 들어오는 간선이 하나도 없는 노드가 없다면, case를 false로 종료한다.
        if root == None:
            isTree = False

        if isTree:
            for nodeItem in nodes.keys():
                # 2. 루트 노드를 제외한 모든 노드는 반드시 단 하나의 들어오는 간선이 존재한다.
                if len(nodes[nodeItem].canIn) != 1 and nodeItem != root:
                    isTree = False
                    break
            # 루트 노드로 들어오는 간선이 존재하면, case를 false로 종료한다.
            if len(nodes[root].canIn) > 0 :
                isTree = False
        
        # 3. 루트에서 다른 노드로 가는 경로는 반드시 가능하며, 유일하다. 이는 루트를 제외한 모든 노드에 성립해야 한다.
        # 1번과 2번을 만족하면, 일단 트리 형태를 만들 수 있는데, 3번 형태가 만족되지 않는 것은 트리에서 연결되지 않은 노드가 존재하지 않는다는 뜻이기 때문에, 트리를 순회하여 Node의 방문하게 되면 canFromRoot을 True값으로 변경하고, 순회가 종료된 뒤에 canFromRoot가 False인 Node가 존재하면 트리가 아니라고 출력한다.
        if not any(data):
            isTree = True
        if isTree and any(data):
            tree = Tree(nodes[root])
            tree.levelorder(nodes[root])
            for nodeItem in nodes.keys():
                if nodes[nodeItem].connectRoot == False:
                    isTree = False
                    break

        if isTree:
             print('case {0} is a tree'.format(testcase_cnt))
        else:
             print('case {0} is not a tree'.format(testcase_cnt))