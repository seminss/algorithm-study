import sys
import heapq

input = sys.stdin.readline
absheap = []

N = int(input())
for _ in range(N) :
    num = int(input())

    if num != 0 : heapq.heappush(absheap,(abs(num),num))
    elif num == 0 and absheap == [] : print(0)
    elif num == 0 and absheap != [] : print(heapq.heappop(absheap)[1])