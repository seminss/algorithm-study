import sys
arr=sys.stdin.readline().strip()
cnt=0
for i in range(len(arr)-1):
    if arr[i]!=arr[i+1]:
        cnt+=1

print((cnt+1)//2)