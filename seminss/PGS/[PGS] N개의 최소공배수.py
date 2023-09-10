def LCM(a,b):
    for i in range(max(a,b),a*b+1):
        if i%a==0 and i%b==0:
            return i
        
def solution(arr):
    a=arr[0]
    b=arr[1]
    answer=LCM(a,b)
    for n in arr[2:]:
        answer=LCM(answer,n)
    return answer