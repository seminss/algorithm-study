import sys
# deque 사용해서 오답 !
import heapq # 자동 정렬 
input = sys.stdin.readline

N = int(input())
lecture = []
priority_queue = []

for i in range(N) :
    S,T = map(int,input().split())
    lecture.append([S,T])

# 시작 시간 순 정렬 
lecture.sort()

heapq.heappush(priority_queue, lecture[0][1])

for l in range(1,N) :

    # 우선순위 큐의 끝나는시간 > 다음 강의 시작시간이라면
    if lecture[l][0] < priority_queue[0] :
        heapq.heappush(priority_queue, lecture[l][1]) # 끝나는 시간을 우선순위 큐에 삽입

    else :
        heapq.heappop(priority_queue) # 강의 끝
        heapq.heappush(priority_queue, lecture[l][1]) # 새로운 강의 끝나는시간 삽입 

print(len(priority_queue))