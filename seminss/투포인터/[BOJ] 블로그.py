import sys

N,X=map(int,sys.stdin.readline().split())
data=list(map(int,sys.stdin.readline().split()))

if max(data)==0:
    print("SAD")
else:
    result=sum(data[:X])
    max_v=result
    cnt=1
    for i in range(X,N):
        result=result-data[i-X]+data[i]
        if max_v<result:
            max_v=result
            cnt=1
        elif max_v==result:
            cnt+=1
    print(max_v)
    print(cnt)
    

# if data[i-X]<data[i]:
#     result=result-data[i-X]+data[i]
#     max_v=result
#     cnt=1
# elif data[i-X]==data[i]:
#     cnt+=1

# data 값을 직접 비교하면 틀린다. 왜일까..?
# 어짜피 data[i-X]==data[i] 이면 result=result-data[i-X]+data[i]가 result=result니까
# result랑 max_value랑 비교하는 식이랑 같은거 아닌가?