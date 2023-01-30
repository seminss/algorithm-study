import sys
N=int(sys.stdin.readline())

queue=[i for i in range(1,N+1)]
front=0 #제일 아래(가장 최근 삭제)
rear=N-1 #제일 위(가장 최근 삽입)

while front!=rear:
    queue[front]=0
    front=(front+1)%N
    tmp=queue[front]
    front=(front+1)%N
    rear=(rear+1)%N
    queue[rear]=tmp
print(queue[front])