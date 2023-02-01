import sys

def searchbinary(arr,start,end):
    while start<=end:
        mid=(start+end)//2
        sub=list(map(lambda x:x-mid,arr))
        positive=list(filter(lambda x:x>0,sub))
        
        if sum(positive)>=k:
            start=mid+1
        else:
            end=mid-1
    return end

n,k=map(int,sys.stdin.readline().split()) #나무개수, 필요한나무m

tree=list(map(int,sys.stdin.readline().split()))
tree.sort()
answer=searchbinary(tree,0,max(tree))
print(answer)
