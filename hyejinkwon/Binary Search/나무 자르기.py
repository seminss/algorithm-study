import sys
N,M = map(int,input().split())
namu_list = list(map(int,input().split()))

start, end = 0, max(namu_list)

while start <= end :
    mid = (start+end) // 2

    sum_height = 0
    for n in namu_list :
        if mid <= n :
            sum_height += (n-mid)

    if sum_height < M :
        end = mid - 1
    else :
        start = mid + 1

print(end)