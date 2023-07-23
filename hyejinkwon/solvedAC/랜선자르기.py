import sys
input = sys.stdin.readline

K, N = map(int, input().split())
length = []
for _ in range(K) :
    length.append(int(input()))
    
# binary search
length.sort()
left = 1
right = length[-1]
max_count = 0

while left <= right :
    mid = (left+right)//2
    count = 0
    
    for l in length :
        count += l//mid
        
    if count >= N :
        left = mid + 1 
    else :
        right = mid - 1
        
print(right)