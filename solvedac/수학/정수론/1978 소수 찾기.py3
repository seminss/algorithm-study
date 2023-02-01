n=int(input())
num_list=list(map(int,input().split()))
cnt=0
for e in num_list:
    if e==1:
        cnt+=1
    for i in range(2,e):
        if e%i==0:
            cnt+=1
            break
print(len(num_list)-cnt)