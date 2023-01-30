import sys
N,M=map(int,sys.stdin.readline().split()) #N:세로, M:가로

c_rule=["BWBWBWBW","WBWBWBWB"]

chess=[0 for i in range(N)]
result=64

for i in range(N):
    M_line=sys.stdin.readline().replace('\n','')
    chess[i]=(M_line)

for j in range(M-7):
    for i in range(N-7):
        b_cnt=0
        w_cnt=0
        cnt=0
        for h in range(8):
            for w in range(8):
                if c_rule[0][w]!=chess[i+h][j+w]:
                    b_cnt+=1
                if c_rule[1][w]!=chess[i+h][j+w]:
                    w_cnt+=1
                cnt=min(b_cnt,w_cnt)
            c_rule.reverse()
        if cnt<result:
            result=cnt
print(result)