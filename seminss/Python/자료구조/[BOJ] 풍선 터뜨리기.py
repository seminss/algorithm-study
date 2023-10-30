# 1:35~2:15

from collections import deque
import sys

n=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()))
queue=deque([(i,arr[i]) for i in range(n)]) #queue로 연산하고 인덱스는 arr에서 조회

while queue:
    idx,step=queue.popleft()
    if step<0 and queue: # 빈 큐 rotate 시 인덱스 에러
        queue.rotate(-1*step)
    elif step>0 and queue:
        queue.rotate(1-step)
    # print(arr.index(step)+1,end=" ") # 중복된 숫자가 있을 경우 조회 문제
    print(idx+1,end=" ")