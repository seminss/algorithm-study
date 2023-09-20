import sys
import heapq

input =sys.stdin.readline
N =int(input())
heap = []

for _ in range(N) :
    comment = int(input())

    if comment == 0 : 
        if heap == [] : 
            print(0)
        else :
            h = heapq.heappop(heap)
            print(h)
    else :
        heapq.heappush(heap, comment)
