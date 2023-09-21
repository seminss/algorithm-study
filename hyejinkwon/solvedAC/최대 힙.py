import sys
import heapq

input = sys.stdin.readline
maxheap = []

N = int(input())
for _ in range(N) :
    num = int(input())

    if num != 0 : heapq.heappush(maxheap, -num)
    elif num == 0 and maxheap == [] : print(0)
    elif num == 0 and maxheap != [] : print(-1*heapq.heappop(maxheap))