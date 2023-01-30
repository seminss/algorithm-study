import sys
N=int(sys.stdin.readline())
p_list=[0 for i in range(N)]

for i in range(N):
    p_list[i]=(tuple(map(int,input().split())))

for e1,e2 in p_list:
    part_cnt=N+1
    for l,w in p_list:
        if not(e1<l and e2<w):
            part_cnt-=1
    print(part_cnt,end=" ")
