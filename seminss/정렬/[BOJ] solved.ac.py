import sys

n=int(sys.stdin.readline())
if n==0:
    print(0)
    exit()

def r_(n):
    if n-int(n)>=0.5:
        return int(n)+1
    else:
        return int(n)

arr=sorted(list(int(sys.stdin.readline()) for _ in range(n)))
del_num=r_(n*0.15)
print(r_(sum(arr[del_num:n-del_num])/(n-del_num*2)))

#기존 round 함수는 1.5도 내림 처리 해버리기 때문에 1.5를 올림 할 수 있는 round 함수를 재구현해야 함.