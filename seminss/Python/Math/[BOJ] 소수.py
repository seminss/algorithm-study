import sys
m=int(sys.stdin.readline())
n=int(sys.stdin.readline())

sq=[True]*(n+1) #기본

for i in range(2,int(n**0.5)+1):
    if sq[i]==True:
        for j in range(i+i,n+1,i):
            sq[j]=False    

sub_sq=[]
for i in range(m,n+1):
    if i>=2:
        if sq[i]==True:
            sub_sq.append(i)
if len(sub_sq)==0:
    print(-1)
else:
    print(sum(sub_sq))
    print(min(sub_sq))
