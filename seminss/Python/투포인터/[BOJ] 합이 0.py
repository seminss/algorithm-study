import sys
from collections import Counter

n=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()))
cnt_dic=Counter(arr)
arr.sort()
team=0

for i in range(n-1,1,-1):
    r_t=i-1
    l_t=0
    while r_t>l_t:
        sum_=arr[r_t]+arr[l_t]+arr[i]
        if sum_==0:
            if arr[l_t]==arr[r_t]: #left와 right가 같은 경우도 고려해야 한다. -4 -4 2 2 2
                team+=r_t-l_t
            else:
                team+=cnt_dic[arr[l_t]]
        if sum_>=0:
            r_t-=1
        else:
            l_t+=1
print(team)

#한 학생을 기준으로 투포인터 구현하는 것까지는 어렵지 않았는데, 중복된 값을 처리하는게 어려웠다..
#중복 값이 연속적으로 나오는 경우를 참고했다.
#counter를 쓰니 비교적 쉽게 구현할 수 있었다..