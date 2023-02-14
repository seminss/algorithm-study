import sys

def searchbinary(arr,start,end):
    while start<=end:
        mid=(start+end)//2
        sub=list(map(lambda x:x-mid,arr)) #arr 각 원소에 접근해서 -mid계산, map->sub array
        positive=list(filter(lambda x:x>0,sub)) #양수인 것만 추출
        # print(mid, positive)
        if sum(positive)>=m:
            start=mid+1
        else:
            end=mid-1
    return end

n,m=map(int,sys.stdin.readline().split()) #나무개수n, 필요한나무m
tree=list(map(int,sys.stdin.readline().split())) #나무 높이

tree.sort() #이진 탐색을 하기 위해 sort
answer=searchbinary(tree,1,max(tree))
print(answer)