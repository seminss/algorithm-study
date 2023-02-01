import sys
testcase=int(input())

for i in range(testcase):
    n,m=map(int,sys.stdin.readline().split())
    queue=list(map(int,sys.stdin.readline().split()))
    cnt=0
    while True:
        m_num=max(queue)
        tmp=queue.pop(0)
        m-=1
        if tmp<m_num: #맨 앞에 젤 큰게 x
            queue.append(tmp)
            if m<0:
                m=len(queue)-1
        else: #맨 앞이 젤 큰거
            cnt+=1
            if m<0:
                print(cnt)
                break