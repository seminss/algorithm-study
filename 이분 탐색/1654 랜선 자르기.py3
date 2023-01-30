import sys

def searchbinary(arr,start,end):
    while start<=end:
        mid=(start+end)//2
        if sum(list(map(lambda x:x//mid,arr)))>=k:
            start=mid+1    
        else:
            end=mid-1
    return end

n,k=map(int,sys.stdin.readline().split())

input_list=[]
for i in range(n):
    input_list.append(int(sys.stdin.readline()))
input_list.sort()

answer=searchbinary(input_list,1,max(input_list))
print(answer)