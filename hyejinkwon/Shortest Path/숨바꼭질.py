import sys
from collections import deque 

input = sys.stdin.readline
time = [0] * 100001
N,K = map(int, input().split())
time[N] = 1

def BFS(N, K) :
    queue = deque()
    queue.append(N)
    
    while queue : 
        V = queue.popleft()

        if V == K : 
            print(time[K]-1)
            break
        
        for i in [V*2, V+1, V-1] :
            if 0 <= i <100001 and time[i] == 0 :
                if i == 2*V : # 순간이동이라면
                    time[i] = time[V]
                    queue.appendleft(i) # 가장 빠른시간을 찾기위해 appendleft이용
                    
                else :
                    time[i] = time[V] + 1
                    queue.append(i)

BFS(N,K)