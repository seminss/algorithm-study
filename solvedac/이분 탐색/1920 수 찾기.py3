import sys

def binary_search(key,arr,low,high):
    while(low<=high):
        middle=(low+high)//2
        if key<arr[middle]:
            high=middle-1
        elif key>arr[middle]:
            low=middle+1
        else:
            print(1)
            return middle
    print(0)
    return


N=int(sys.stdin.readline())
old=list(map(int,sys.stdin.readline().split()))

M=int(sys.stdin.readline())
new=list(map(int,sys.stdin.readline().split()))

old.sort()
for i in range(M):
    binary_search(new[i],old,0,N-1)