#파이썬은 초당 2000만번 연산
import sys
n,k=map(int,sys.stdin.readline().split())

arr=list(map(int,sys.stdin.readline().split()))
head,tail,odd,asw=0,0,0,0

while tail<len(arr):
    if odd>k:
        if arr[head]%2!=0:
            odd-=1 #여기 해당되지 않으면 아래 if 문에도 안걸림, 결국 head가 홀수가 될때까지 계속 head는 +1
        head+=1
    else:
        if arr[tail]%2!=0:
            odd+=1
        tail+=1
    if odd<=k: #홀수가 k개 이하여도 가장 긴 짝수 배열이 나올 수 있다.
        asw=max(asw,tail-head-odd)
print(asw)