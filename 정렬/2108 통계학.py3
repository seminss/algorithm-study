import sys
from collections import Counter

n=int(sys.stdin.readline())

arr=[] #입력값으로 배열 채우기
for _ in range(n):
    arr.append(int(sys.stdin.readline()))

#산술평균
print(round(sum(arr)/n))#소숫점 출력

#중앙값
arr.sort()
print(arr[(n-1)//2])

#최빈값
cnt=Counter(arr).most_common(2)
if len(arr)>1:
    if cnt[0][1]==cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])

#범위
print(arr[-1]-arr[0])